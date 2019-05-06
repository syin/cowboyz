<cowboyz>
    <div class="container">
        <div class="box input">
            <img if={ input_img } src="/static/assets/ios/{ input_img.name }.png" alt="">
            <div if={ show_emoji_picker }></div>
        </div>
        <div class="transform">
            <span class="arrow">&#x27A1;</span>
            <span>yeehaw</span>
        </div>
        <div class="box output">
            <img if={ cowboized_img } src="/static/output/{ cowboized_img.name }_cowboyz.png" alt="">
        </div>
    </div>

    <script>
        self = this;
        self.available_emojis = [];
        self.input_img = {
            'name': 'hugging-face-1f917',
        };
        self.cowboized_img = undefined;
        self.show_emoji_picker = false;

        cowboizeEmoji() {
            const apiUrl = `/api/cowboize/${self.input_img.name}`;
            fetch(apiUrl).then(response => {
                response.json().then(data => {
                    self.cowboized_img = data;
                    self.update();
                });
            }).catch(error => {
                console.log('error', error);
            });
        }

        getEmojiList() {
            const apiUrl = '/api/list';
            fetch(apiUrl).then(response => {
                response.json().then(data => {
                    self.available_emojis = data;
                });
            }).catch(error => {
                console.log('error', error);
            });
        }

        self.getEmojiList();
        self.cowboizeEmoji();
    </script>
</cowboyz>
