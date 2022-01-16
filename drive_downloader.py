import argparse
import getpass
from google_drive_downloader import GoogleDriveDownloader

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='URL for the Drive File')
    parser.add_argument('-p', '--path', help='Local path with filename to save file\nFor Example C://Users//xyz//Downloads//abc.txt')
    args = parser.parse_args()
    if args.url:
        url = args.url
        if args.path:
            path = args.path        
            file_id = url.split('/')[5]
            GoogleDriveDownloader.download_file_from_google_drive(file_id=file_id, dest_path=path, overwrite=True)
        else:
            print("No Destination Path Found Exiting.....")
            exit(0)
    else:
        print("No URL Provided, Exiting.....")
        exit(0)
        

