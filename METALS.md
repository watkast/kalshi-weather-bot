# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 12:31 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 101 | 101 | 32 (32%) | 39¢ | 47% | -$94.04 | -23% |
| Silver | 51 | 51 | 15 (29%) | 34¢ | 42% | -$30.39 | -17% |
| Gold | 50 | 50 | 17 (34%) | 45¢ | 53% | -$63.65 | -27% |

*Earlier half -$44.67 / later half -$49.37.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 104 | 33 (32%) | -$106.01 | -24% |
| 4¢+ ← live bot | 101 | 34 (34%) | -$38.22 | -10% |
| 6¢+ | 89 | 35 (39%) | $45.95 | +15% |
| 8¢+ | 76 | 31 (41%) | $66.56 | +27% |
| 10¢+ | 63 | 22 (35%) | $26.88 | +14% |
| 15¢+ | 36 | 13 (36%) | $36.72 | +39% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2588 | -1.7% |
| Hyperliquid price vs Kalshi's target | 2588 | +1.2% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:22:09 PM | Silver | UP | 7.8 min | 29¢ | 39% | 9¢ | ❌ Lost | -$3.05 |
| 9/29 12:16:11 PM | Gold | DOWN | 13.8 min | 36¢ | 44% | 6¢ | ✅ Won | $6.23 |
| 9/29 12:01:02 PM | Gold | UP | 13.9 min | 91¢ | 96% | 4¢ | ✅ Won | $0.84 |
| 9/29 11:47:34 AM | Silver | UP | 12.4 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/29 11:46:56 AM | Gold | UP | 13.1 min | 40¢ | 47% | 5¢ | ❌ Lost | -$4.17 |
| 9/29 11:32:32 AM | Gold | UP | 12.4 min | 34¢ | 46% | 10¢ | ❌ Lost | -$3.56 |
| 9/29 11:32:10 AM | Silver | UP | 12.8 min | 32¢ | 41% | 7¢ | ❌ Lost | -$3.36 |
| 9/29 11:19:27 AM | Gold | DOWN | 10.5 min | 35¢ | 41% | 5¢ | ❌ Lost | -$3.66 |
| 9/29 11:16:05 AM | Silver | DOWN | 13.9 min | 41¢ | 48% | 6¢ | ❌ Lost | -$4.27 |
| 9/29 11:01:35 AM | Silver | DOWN | 13.4 min | 36¢ | 44% | 6¢ | ❌ Lost | -$3.77 |
| 9/29 11:01:13 AM | Gold | DOWN | 13.8 min | 45¢ | 52% | 5¢ | ❌ Lost | -$4.68 |
| 9/29 10:50:18 AM | Silver | DOWN | 9.7 min | 29¢ | 36% | 6¢ | ✅ Won | $6.95 |
