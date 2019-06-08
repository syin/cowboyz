<cowboyz>
    <div class="container">
        <div class="box input">
            <div onclick={ showEmojiPicker } class="input-wrapper">
                <img if={ input_img } src="/static/assets/ios/{ input_img.name }.png" alt="" class="input-img">
            </div>
            <div ref="emojiPicker" if={ show_emoji_picker && available_emojis.length } tabindex="0" class="emoji-picker">
                <div class="emoji-picker-content">
                    <img each={ name in available_emojis } data-emoji-name={ name } onclick={ selectEmoji } src="/static/assets/ios/{ name }.png" alt="">
                </div>
            </div>
        </div>
        <div class="transform">
            <span class="arrow"></span>
            <span ref="yeehaw" class="yeehaw">yeehaw</span>
        </div>
        <div class="box output">
            <img if={ cowboized_img } ref="cowboizedImg" src="/static/output/{ cowboized_img.name }_cowboyz.png" alt="">
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

        showEmojiPicker(e) {
            e.stopPropagation();
            self.show_emoji_picker = true;
            self.update();
            self.refs.emojiPicker.focus();
        }

        hideEmojiPicker() {
            self.show_emoji_picker = false;
            self.update();
        }

        selectEmoji(e) {
            const selectedEmojiName = e.target.dataset.emojiName;
            self.input_img = {
                'name': selectedEmojiName,
            };
            self.cowboized_img = undefined;
            self.cowboizeEmoji();
            self.yeehawAnimation();
        }

        yeehawAnimation() {
            console.log('self.refs.yeehaw.classList', self.refs.yeehaw.classList);
            self.refs.yeehaw.classList.add("show");
            setTimeout(function() {
                self.refs.yeehaw.classList.remove("show");
            }, 1000);
        }

        document.addEventListener("click", (e) => {
            self.hideEmojiPicker();
        });

        self.getEmojiList();
        self.cowboizeEmoji();
    </script>
</cowboyz>
