# lab_kuber_tools №10
1. Перед началом работы удаляются старые ресурсы из кластера
  <img width="580" height="113" alt="image" src="https://github.com/user-attachments/assets/f729db7a-54b3-4b89-908a-f9537010a88b" />
  <img width="709" height="283" alt="image" src="https://github.com/user-attachments/assets/03ad24f1-1615-45d3-b932-60d95bb4f2da" />

2. За основу берется работа из темы docker-compose
   <img width="532" height="349" alt="image" src="https://github.com/user-attachments/assets/efd58bdb-f480-4ce7-a8ce-6489309ca3a5" />

3. Устанавливаем Helm

   <img width="838" height="210" alt="image" src="https://github.com/user-attachments/assets/a815075a-ab44-4675-835d-03d5c0c6b13e" />

4. Устанавливаем Kompose

     <img width="826" height="193" alt="image" src="https://github.com/user-attachments/assets/dcf03f9d-7251-4861-813b-389f3858c912" />

5. Конвертируем compose манифест в k8s ресурсы

   <img width="820" height="452" alt="image" src="https://github.com/user-attachments/assets/de246253-a1ed-4177-b208-e28e9f7c968a" />
   <img width="823" height="350" alt="image" src="https://github.com/user-attachments/assets/6f7282e9-1768-4bfd-b513-0758acb17ff3" />

6. Теперь конкретно конвертируем compose манифест helm chart

   <img width="818" height="589" alt="image" src="https://github.com/user-attachments/assets/56d7d30b-9898-456b-9973-8467cb997e3e" />

7. После конвертации добавляются новые файлы в templates/

   <img width="727" height="387" alt="image" src="https://github.com/user-attachments/assets/37b58d25-388e-44b1-9b96-3d8098f95a89" />

8. Правим название чарта в файле Chart.yaml на promgra, а также переименовываем полностью каталог из compose в promgra

   <img width="809" height="313" alt="image" src="https://github.com/user-attachments/assets/76432eda-afa6-4165-8ec6-61668bf9f356" />
    <img width="562" height="361" alt="image" src="https://github.com/user-attachments/assets/c343a665-4d8e-457d-9d2e-ff671a635bb2" />

9. Упаковали чарт, а также применили изменения и посмотрели статус minikube

   <img width="830" height="94" alt="image" src="https://github.com/user-attachments/assets/08723b91-8adc-4812-a4c3-f5ff9bb0f033" />
   <img width="813" height="622" alt="image" src="https://github.com/user-attachments/assets/2061d1fa-d5f7-4bd4-94fb-414e07cc10ce" />

10. Устанавливаем релиз с именем promgra из локального чарт файла tgz

    <img width="862" height="187" alt="image" src="https://github.com/user-attachments/assets/bc5eff51-4d79-4fcc-bd3e-64ddd6e77309" />
    <img width="754" height="143" alt="image" src="https://github.com/user-attachments/assets/5d4001a0-653b-4496-a52b-50fb31c10c38" />

11.  Выгрузили образ, пробросили порты, перебросили туннель, попали в графану

   <img width="1280" height="500" alt="image" src="https://github.com/user-attachments/assets/46d0820b-dc70-46da-86df-a6f875c4cf2c" />

12.  Добавляем values к чарту, создаем values.yaml

  <img width="439" height="261" alt="image" src="https://github.com/user-attachments/assets/2def3509-7d95-4b31-a52f-e946a1b1e29c" />

13. Апгрейдим релиз с новыми значениями

    <img width="851" height="582" alt="image" src="https://github.com/user-attachments/assets/6d296b5a-0a0e-4192-8c4a-093e70039be3" />

14. Пробрасываем порт 3456 и попадаем в Grafana

    <img width="1018" height="583" alt="image" src="https://github.com/user-attachments/assets/981c2efb-67d6-4ed9-a18c-5b7544f72b74" />

15. Выполняем демонтаж релиза

    <img width="843" height="76" alt="image" src="https://github.com/user-attachments/assets/38c6e9e5-4f31-493d-b77a-82e031c4edc3" />

16. Далее необходимо развернуть две инсталяции в prod и dev из одного проекта flask-redis. Для этого переносим манифесты в отдельный каталог base

    <img width="494" height="291" alt="image" src="https://github.com/user-attachments/assets/dce30568-5a32-4908-aac5-f376efcca077" />

17. Затем внутри base создаем kustomization.yaml, являющийся базовой кастомизацией для всех ресурсов всех окружений

    <img width="623" height="295" alt="image" src="https://github.com/user-attachments/assets/fb06f489-9e1f-4661-9cdb-4d12ce68f525" />

18. Применяем без развертывания

    <img width="674" height="478" alt="image" src="https://github.com/user-attachments/assets/68b8927f-0263-437b-b53f-df2fc3a04ec5" />

19. Затем создаем доп кастомизации поверх base для dev и prod и применяем

    а) Для dev

    <img width="632" height="270" alt="image" src="https://github.com/user-attachments/assets/91dd865d-5d23-4e57-a7a7-e3e5b4bcf2c5" />
    <img width="640" height="726" alt="image" src="https://github.com/user-attachments/assets/64c83a96-d5e4-4868-b866-4befd23df2a7" />

    б) Для prod

    <img width="591" height="373" alt="image" src="https://github.com/user-attachments/assets/61f692f7-1f95-4f34-a4b3-c15a20ae85f8" />
    <img width="621" height="671" alt="image" src="https://github.com/user-attachments/assets/d1c17cc0-995a-45eb-b0de-8155201ef62a" />

20. Выполняем кастомизацию со ссылкой на патч, а также меняем порт в окружении dev

    <img width="612" height="183" alt="image" src="https://github.com/user-attachments/assets/7a22999b-d6b8-4bab-aa68-028c1f884d40" />

21. Результат применения патча: замена порта

    <img width="349" height="188" alt="image" src="https://github.com/user-attachments/assets/803d6e3e-4c3c-4a03-a024-768121882607" />

22. Применяем в кластер манифесты с dev и prod кастомизацией

    <img width="859" height="451" alt="image" src="https://github.com/user-attachments/assets/b20dcc3d-e836-480c-9018-a9188659dc17" />
    <img width="797" height="704" alt="image" src="https://github.com/user-attachments/assets/cec346bd-1ce2-4f4b-acaf-125a612832e6" />

23. Кастомизируем количество реплик в dev окружении

    <img width="710" height="611" alt="image" src="https://github.com/user-attachments/assets/e8676f80-a243-40fc-99e6-84bdf621d216" />

24. А далее у меня пошли проблемы скорее всего с портами, опять отваливался интернет на ВМ, как при первых лабораторных. Я пробовала и переброс портов в самом virtual-box, также port-forwarding, затем открывать локально на ВМ через разные порты, которые отображаются в сервисах и в своих настройках файлов. Не получилось запустить приложение, а уже не хватило терпения, сил и мозгов для фикса этой проблемы :(
