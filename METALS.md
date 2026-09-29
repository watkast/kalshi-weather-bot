# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 11:31 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🟡 **Mixed.** Up overall, but not in both halves — could be luck.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 34 | 34 | 14 (41%) | 39¢ | 48% | $0.56 | +0% |
| Silver | 17 | 17 | 6 (35%) | 32¢ | 41% | $2.40 | +4% |
| Gold | 17 | 17 | 8 (47%) | 46¢ | 54% | -$1.84 | -2% |

*Earlier half $25.18 / later half -$24.62.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 34 | 11 (32%) | -$35.21 | -24% |
| 4¢+ ← live bot | 33 | 11 (33%) | -$13.07 | -11% |
| 6¢+ | 31 | 10 (32%) | $0.94 | +1% |
| 8¢+ | 29 | 10 (34%) | $14.70 | +17% |
| 10¢+ | 26 | 7 (27%) | $2.33 | +3% |
| 15¢+ | 12 | 4 (33%) | $13.32 | +50% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 847 | -4.0% |
| Hyperliquid price vs Kalshi's target | 847 | -19.1% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 11:18:01 PM | Silver | DOWN | 12.0 min | 28¢ | 46% | 16¢ | ✅ Won | $7.05 |
| 9/28 11:17:37 PM | Gold | DOWN | 12.4 min | 58¢ | 66% | 6¢ | ❌ Lost | -$5.98 |
| 9/28 11:02:38 PM | Gold | UP | 12.4 min | 65¢ | 73% | 7¢ | ✅ Won | $3.34 |
| 9/28 11:01:02 PM | Silver | DOWN | 13.9 min | 31¢ | 39% | 6¢ | ❌ Lost | -$3.25 |
| 9/28 10:52:13 PM | Silver | DOWN | 7.8 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 10:47:04 PM | Gold | UP | 12.9 min | 52¢ | 59% | 5¢ | ❌ Lost | -$5.38 |
| 9/28 10:31:35 PM | Silver | DOWN | 13.4 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/28 10:31:31 PM | Gold | UP | 13.5 min | 59¢ | 68% | 7¢ | ❌ Lost | -$6.07 |
| 9/28 10:16:38 PM | Silver | DOWN | 13.4 min | 40¢ | 51% | 9¢ | ❌ Lost | -$4.17 |
| 9/28 10:16:04 PM | Gold | UP | 13.9 min | 37¢ | 43% | 4¢ | ❌ Lost | -$3.87 |
| 9/28 10:01:37 PM | Silver | UP | 13.4 min | 32¢ | 39% | 5¢ | ❌ Lost | -$3.36 |
| 9/28 10:01:05 PM | Gold | UP | 13.9 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
