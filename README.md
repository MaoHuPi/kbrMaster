# kbrMaster｜簡易鍵盤監聽器

> 2023 © MaoHuPi

## 注意事項

1. 對於有需要透過記錄鍵盤事件來取得他人輸入於自己之電腦之密碼之人，方可使用此程式
2. 此程式並非電腦病毒，因此並未實作任何偽裝、傳播、自行啟動的功能，因此不要拿它來當病毒植入他人電腦
3. 請不要嘗試在班用電腦使用此程式，否則可能會被我舉發

## 使用方式

1. 打開「設定」
2. 開啟「隱私權與安全性」
3. 點擊「Windows安全性」
4. 點擊「病毒與威脅防護」
5. 點擊下圖對應之位置中的「Manage settings」

  ![image](https://user-images.githubusercontent.com/60348735/218481638-e77253ed-3af3-4447-9566-baebd6225ad3.png)
  
6. 將下圖對應之位置中的「即時防護」選項關閉(如圖中狀態)

  ![image](https://user-images.githubusercontent.com/60348735/218481826-a8944cae-5799-4a40-a295-bb0e7417b816.png)
  
7. 點擊「[連結](https://github.com/MaoHuPi/kbrMaster/blob/main/kbrMaster.exe?raw=true)」來下載執行檔
8. 去下載檔案的存放位置解壓縮，並將執行檔放置喜歡的位置
9. 點兩下執行檔執行
10. 獲取到的鍵盤事件將顯示於Terminal(cmd or powershell or something that I don't very care about it)視窗，並同時記錄至與執行檔同層的「kbr.log」純文字檔案中
11. 點擊Terminal視窗的關閉按鈕(x)即可停止鍵盤監聽
