import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from time import sleep

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    while(True):

        try:
            # Youtube request
            request = youtube.videos().list(
                part="snippet,statistics",
                id="youtube-video-id"
            )
            response = request.execute()

            data = response["items"][0]
            vid_snippet = data["snippet"]

            title = vid_snippet["title"]

            views = str(data["statistics"]["viewCount"])

            print("")
            print("Title of Video: " + title)
            print("Number of Views: " + views)

            change = (views not in title)

            # Updating
            if(change):
                title_upd = f"This video has {views} views"
                vid_snippet["title"] = title_upd

                request = youtube.videos().update(
                    part="snippet",
                    body={
                        "id": "nzJido1Uhew",
                        "snippet": vid_snippet
                    }
                )
                response = request.execute()
                print("Updated!")

            print("Worked!")
            sleep(60*10)
        except Exception:
            print("Didn't work!")


if __name__ == "__main__":
    main()
