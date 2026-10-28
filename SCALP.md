# Range-Scalp Bot

*Updated Wed Oct 28 03:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37520 | 32750 | 4770 (45) | 2 | $-10484.75 | -4.4% |
| **+10¢** | 28014 | 22491 | 5523 (67) | 3 | $-9353.21 | -5.3% |
| **+15¢** | 23435 | 17505 | 5930 (91) | 4 | $-8309.86 | -5.6% |
| **+20¢** | 20773 | 14566 | 6207 (116) | 5 | $-7281.23 | -5.6% |
| **+10¢ (15¢ stop)** | 45948 | 45883 | 65 (34) | 3 | $-17473.73 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 03:34 | +5 | DOGE | UP | 0.61 | open |  |
| 10-28 03:33 | +5 | HYPE | DOWN | 0.60 | open |  |
| 10-28 03:33 | +10 stop | NEAR | UP | 0.59 | open |  |
| 10-28 03:33 | +10 | NEAR | UP | 0.59 | open |  |
| 10-28 03:33 | +5 | NEAR | UP | 0.59 | 0.65 | 0.27 |
| 10-28 03:33 | +10 stop | DOGE | UP | 0.58 | open |  |
| 10-28 03:33 | +20 | DOGE | UP | 0.58 | open |  |
| 10-28 03:33 | +15 | DOGE | UP | 0.58 | open |  |
| 10-28 03:33 | +10 | DOGE | UP | 0.58 | open |  |
| 10-28 03:33 | +5 | DOGE | UP | 0.58 | 0.63 | 0.15 |
| 10-28 03:33 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 10-28 03:32 | +10 stop | HYPE | DOWN | 0.57 | 0.42 | -1.86 |
| 10-28 03:32 | +20 | HYPE | DOWN | 0.57 | open |  |
| 10-28 03:32 | +15 | HYPE | DOWN | 0.57 | open |  |
| 10-28 03:32 | +10 | HYPE | DOWN | 0.57 | open |  |
| 10-28 03:32 | +5 | HYPE | DOWN | 0.57 | 0.64 | 0.35 |
| 10-28 03:31 | +10 stop | ZEC | UP | 0.58 | 0.93 | 3.27 |
| 10-28 03:31 | +20 | ZEC | UP | 0.58 | 0.93 | 3.27 |
| 10-28 03:31 | +15 | ZEC | UP | 0.58 | 0.93 | 3.27 |
| 10-28 03:31 | +10 | ZEC | UP | 0.59 | 0.93 | 3.18 |
| 10-28 03:31 | +5 | ZEC | UP | 0.59 | 0.93 | 3.18 |
| 10-28 03:31 | +10 stop | BNB | UP | 0.71 | 0.84 | 1.05 |
| 10-28 03:31 | +20 | BNB | UP | 0.71 | open |  |
| 10-28 03:31 | +15 | BNB | UP | 0.71 | open |  |
| 10-28 03:31 | +10 | BNB | UP | 0.71 | 0.84 | 1.05 |
| 10-28 03:31 | +5 | BNB | UP | 0.71 | 0.84 | 1.05 |
| 10-28 03:30 | +10 stop | NEAR | UP | 0.66 | 0.79 | 1.02 |
| 10-28 03:30 | +20 | NEAR | UP | 0.66 | open |  |
| 10-28 03:30 | +15 | NEAR | UP | 0.66 | open |  |
| 10-28 03:30 | +10 | NEAR | UP | 0.66 | 0.79 | 1.03 |
| 10-28 03:30 | +5 | NEAR | UP | 0.65 | 0.79 | 1.12 |
| 10-28 03:30 | +10 stop | BTC | UP | 0.68 | 0.85 | 1.45 |
| 10-28 03:30 | +20 | BTC | UP | 0.68 | open |  |
| 10-28 03:30 | +15 | BTC | UP | 0.66 | 0.85 | 1.65 |
| 10-28 03:30 | +10 | BTC | UP | 0.66 | 0.77 | 0.81 |
| 10-28 03:30 | +5 | BTC | UP | 0.66 | 0.71 | 0.19 |
| 10-28 03:25 | +10 | HYPE | DOWN | 0.70 | yes | -7.19 |
| 10-28 03:25 | +5 | HYPE | DOWN | 0.70 | yes | -7.19 |
| 10-28 03:25 | +10 stop | XRP | DOWN | 0.54 | 0.64 | 0.65 |
| 10-28 03:25 | +10 stop | HYPE | DOWN | 0.61 | 0.39 | -2.58 |
