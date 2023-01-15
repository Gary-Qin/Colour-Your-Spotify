import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

def Main():
    print("Main Menu")
    print("\n1 - Login")
    print("2 - Create new user")
    
    selection = False
    while selection == False:
        usrChoice = input("\nEnter a selection: ")
        if usrChoice == '1':
            login()
            selection = True
        elif usrChoice == '2':
            create_user()
            selection = True
        else:
            print('Please enter either "1" or "2"')


def create_user():
    name = input("Enter your name: ")

def login():

    webcam = cv2.VideoCapture(0)

    detector = FaceMeshDetector(maxFaces = 1)

    plotY = LivePlot(960,760, [10,50])

    id_list = []

    for num in range(0,468):
        id_list.append(num)

    #id_list = [0, 16, 61, 306]

    while True:

        success, img = webcam.read()

        if success == True:
            img, faces = detector.findFaceMesh(img, draw = False)

            if faces:
                face = faces[0]
        
                for id in id_list:
                    cv2.circle(img, face[id], 1, (255,0,255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img, str(id), face[id], font, 0.21,(255,255,255),1)
                
                top = face[0]
                bottom = face[16]
                left = face[61]
                right = face[306]

                vertical, unused = detector.findDistance(top, bottom)
                horizontal, unsused = detector.findDistance(left, right)

                cv2.line(img, top, bottom, (0,200,0), 1)
                cv2.line(img, left, right, (0,200,0), 1)

                ratio = (vertical/horizontal)*100

                img_plot = plotY.update(ratio)

            try:
                img = cv2.resize(img, (960,760))
                cv2.imshow("ImgPlot", img_plot)
                cv2.imshow("Webcam", img)
                key = cv2.waitKey(1)
            except NameError:
                print("No face detected")

if __name__ == "__main__":
    Main()