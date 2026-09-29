# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 1:31 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 110 | 109 | 36 (33%) | 39¢ | 47% | -$85.05 | -19% |
| Silver | 55 | 55 | 17 (31%) | 34¢ | 42% | -$25.55 | -13% |
| Gold | 55 | 54 | 19 (35%) | 45¢ | 52% | -$59.50 | -24% |

*Earlier half -$35.75 / later half -$49.30.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 112 | 37 (33%) | -$99.06 | -21% |
| 4¢+ ← live bot | 109 | 38 (35%) | -$28.94 | -7% |
| 6¢+ | 97 | 40 (41%) | $67.48 | +20% |
| 8¢+ | 84 | 36 (43%) | $90.76 | +34% |
| 10¢+ | 71 | 27 (38%) | $54.28 | +25% |
| 15¢+ | 42 | 15 (36%) | $41.86 | +39% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2790 | -0.7% |
| Hyperliquid price vs Kalshi's target | 2790 | +2.1% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 1:31:03 PM | Gold | UP | 13.9 min | 36¢ | 50% | 12¢ | Open | — |
| 9/29 1:19:47 PM | Silver | DOWN | 10.2 min | 33¢ | 44% | 9¢ | ❌ Lost | -$3.46 |
| 9/29 1:16:19 PM | Gold | DOWN | 13.7 min | 46¢ | 54% | 6¢ | ❌ Lost | -$4.78 |
| 9/29 1:02:33 PM | Gold | UP | 12.4 min | 41¢ | 48% | 5¢ | ❌ Lost | -$4.27 |
| 9/29 1:02:03 PM | Silver | UP | 12.9 min | 41¢ | 47% | 4¢ | ❌ Lost | -$4.27 |
| 9/29 12:46:21 PM | Gold | UP | 13.7 min | 41¢ | 50% | 7¢ | ✅ Won | $5.73 |
| 9/29 12:46:03 PM | Silver | UP | 13.9 min | 39¢ | 50% | 9¢ | ✅ Won | $5.93 |
| 9/29 12:33:37 PM | Gold | UP | 11.4 min | 24¢ | 35% | 10¢ | ✅ Won | $7.47 |
| 9/29 12:32:31 PM | Silver | UP | 12.5 min | 32¢ | 39% | 5¢ | ✅ Won | $6.64 |
| 9/29 12:22:09 PM | Silver | UP | 7.8 min | 29¢ | 39% | 9¢ | ❌ Lost | -$3.05 |
| 9/29 12:16:11 PM | Gold | DOWN | 13.8 min | 36¢ | 44% | 6¢ | ✅ Won | $6.23 |
| 9/29 12:01:02 PM | Gold | UP | 13.9 min | 91¢ | 96% | 4¢ | ✅ Won | $0.84 |
