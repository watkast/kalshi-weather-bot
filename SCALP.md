# Range-Scalp Bot

*Updated Tue Nov 03 02:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45459 | 39579 | 5880 (67) | 2 | $-13161.38 | -4.6% |
| **+10¢** | 33929 | 27116 | 6813 (89) | 2 | $-12047.99 | -5.6% |
| **+15¢** | 28382 | 21052 | 7330 (116) | 2 | $-11082.35 | -6.2% |
| **+20¢** | 25207 | 17531 | 7676 (151) | 2 | $-9838.71 | -6.2% |
| **+10¢ (15¢ stop)** | 55465 | 55378 | 87 (51) | 2 | $-20926.27 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 02:01 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 11-03 02:01 | +20 | HYPE | DOWN | 0.70 | open |  |
| 11-03 02:01 | +15 | HYPE | DOWN | 0.69 | open |  |
| 11-03 02:01 | +10 | HYPE | DOWN | 0.69 | open |  |
| 11-03 02:01 | +5 | HYPE | DOWN | 0.69 | open |  |
| 11-03 02:01 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 11-03 02:01 | +20 | BTC | DOWN | 0.70 | open |  |
| 11-03 02:01 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-03 02:01 | +10 | BTC | DOWN | 0.70 | open |  |
| 11-03 02:01 | +5 | BTC | DOWN | 0.70 | open |  |
| 11-03 01:57 | +10 stop | BTC | DOWN | 0.53 | 0.64 | 0.75 |
| 11-03 01:57 | +20 | BTC | DOWN | 0.54 | 0.78 | 2.09 |
| 11-03 01:57 | +15 | BTC | DOWN | 0.54 | 0.78 | 2.14 |
| 11-03 01:57 | +10 | BTC | DOWN | 0.53 | 0.64 | 0.75 |
| 11-03 01:57 | +5 | BTC | DOWN | 0.53 | 0.64 | 0.75 |
| 11-03 01:57 | +10 stop | DOGE | DOWN | 0.64 | 0.82 | 1.52 |
| 11-03 01:57 | +20 | DOGE | DOWN | 0.64 | 0.86 | 1.94 |
| 11-03 01:57 | +15 | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-03 01:57 | +10 | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-03 01:57 | +5 | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-03 01:56 | +10 stop | XRP | DOWN | 0.63 | 0.77 | 1.10 |
| 11-03 01:55 | +10 stop | XRP | UP | 0.63 | 0.41 | -2.54 |
| 11-03 01:55 | +20 | XRP | UP | 0.62 | no | -6.37 |
| 11-03 01:55 | +15 | XRP | UP | 0.63 | no | -6.47 |
| 11-03 01:55 | +10 | XRP | UP | 0.62 | no | -6.37 |
| 11-03 01:55 | +5 | XRP | UP | 0.62 | no | -6.37 |
| 11-03 01:53 | +10 stop | HYPE | UP | 0.66 | 0.40 | -2.97 |
| 11-03 01:52 | +10 stop | XRP | UP | 0.60 | 0.79 | 1.61 |
| 11-03 01:51 | +10 stop | BNB | UP | 0.70 | 0.82 | 0.94 |
| 11-03 01:51 | +20 | BNB | UP | 0.70 | 0.93 | 2.05 |
| 11-03 01:51 | +15 | BNB | UP | 0.70 | 0.93 | 2.05 |
| 11-03 01:51 | +10 | BNB | UP | 0.71 | 0.82 | 0.84 |
| 11-03 01:51 | +5 | BNB | UP | 0.70 | 0.75 | 0.21 |
| 11-03 01:50 | +10 stop | XRP | UP | 0.50 | 0.60 | 0.65 |
| 11-03 01:49 | +10 stop | NEAR | UP | 0.56 | 0.37 | -2.25 |
| 11-03 01:49 | +10 | NEAR | UP | 0.56 | no | -5.78 |
| 11-03 01:49 | +5 | BNB | UP | 0.59 | 0.74 | 1.19 |
| 11-03 01:48 | +10 stop | BTC | UP | 0.64 | 0.76 | 0.90 |
| 11-03 01:48 | +15 | BTC | UP | 0.63 | 0.79 | 1.31 |
| 11-03 01:48 | +10 | BTC | UP | 0.63 | 0.73 | 0.69 |
