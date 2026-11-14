# Range-Scalp Bot

*Updated Sat Nov 14 08:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59190 | 51640 | 7550 (107) | 0 | $-16017.24 | -4.3% |
| **+10¢** | 44222 | 35388 | 8834 (140) | 0 | $-15034.88 | -5.4% |
| **+15¢** | 37055 | 27529 | 9526 (176) | 0 | $-13685.37 | -5.9% |
| **+20¢** | 33008 | 23008 | 10000 (228) | 1 | $-12077.58 | -5.8% |
| **+10¢ (15¢ stop)** | 72041 | 71899 | 142 (82) | 0 | $-26511.09 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 08:12 | +10 stop | HYPE | UP | 0.70 | 0.54 | -1.92 |
| 11-14 08:12 | +20 | HYPE | UP | 0.70 | no | -7.15 |
| 11-14 08:12 | +15 | HYPE | UP | 0.70 | no | -7.13 |
| 11-14 08:12 | +10 | HYPE | UP | 0.70 | 0.81 | 0.86 |
| 11-14 08:12 | +10 stop | NEAR | DOWN | 0.41 | 0.54 | 0.95 |
| 11-14 08:12 | +5 | HYPE | UP | 0.71 | 0.79 | 0.53 |
| 11-14 08:09 | +10 stop | NEAR | UP | 0.63 | 0.39 | -2.74 |
| 11-14 08:09 | +5 | BNB | UP | 0.59 | 0.69 | 0.68 |
| 11-14 08:08 | +10 stop | BNB | UP | 0.56 | 0.69 | 0.97 |
| 11-14 08:08 | +10 | BNB | UP | 0.56 | 0.69 | 0.97 |
| 11-14 08:08 | +5 | BNB | UP | 0.56 | 0.64 | 0.45 |
| 11-14 08:08 | +10 stop | HYPE | UP | 0.58 | 0.71 | 0.97 |
| 11-14 08:08 | +5 | HYPE | UP | 0.58 | 0.71 | 0.97 |
| 11-14 08:07 | +10 stop | ZEC | DOWN | 0.49 | 0.64 | 1.15 |
| 11-14 08:07 | +15 | ZEC | DOWN | 0.49 | 0.64 | 1.15 |
| 11-14 08:07 | +10 | ZEC | DOWN | 0.49 | 0.64 | 1.15 |
| 11-14 08:07 | +5 | ZEC | DOWN | 0.49 | 0.64 | 1.15 |
| 11-14 08:06 | +10 stop | NEAR | DOWN | 0.69 | 0.47 | -2.53 |
| 11-14 08:05 | +5 | BNB | UP | 0.66 | 0.77 | 0.81 |
| 11-14 08:05 | +5 | XRP | UP | 0.69 | 0.79 | 0.73 |
| 11-14 08:04 | +10 stop | NEAR | DOWN | 0.57 | 0.67 | 0.66 |
| 11-14 08:04 | +10 stop | BNB | UP | 0.56 | 0.77 | 1.79 |
| 11-14 08:04 | +5 | BNB | UP | 0.55 | 0.62 | 0.35 |
| 11-14 08:03 | +10 stop | XRP | UP | 0.65 | 0.79 | 1.12 |
| 11-14 08:03 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-14 08:03 | +10 stop | BTC | UP | 0.58 | 0.70 | 0.87 |
| 11-14 08:03 | +10 stop | DOGE | DOWN | 0.63 | 0.47 | -1.95 |
| 11-14 08:02 | +10 stop | XRP | DOWN | 0.43 | 0.55 | 0.84 |
| 11-14 08:02 | +10 stop | ETH | DOWN | 0.54 | 0.16 | -4.08 |
| 11-14 08:02 | +10 stop | HYPE | DOWN | 0.61 | 0.34 | -3.03 |
| 11-14 08:02 | +10 stop | NEAR | DOWN | 0.67 | 0.52 | -1.84 |
| 11-14 08:02 | +20 | NEAR | DOWN | 0.67 | 0.98 | 2.88 |
| 11-14 08:02 | +15 | NEAR | DOWN | 0.67 | 0.98 | 2.88 |
| 11-14 08:02 | +10 | NEAR | DOWN | 0.67 | 0.98 | 2.88 |
| 11-14 08:02 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
| 11-14 08:01 | +10 stop | ZEC | DOWN | 0.63 | 0.48 | -1.85 |
| 11-14 08:01 | +20 | ZEC | DOWN | 0.63 | open |  |
| 11-14 08:01 | +15 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-14 08:01 | +10 | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-14 08:01 | +5 | ZEC | DOWN | 0.63 | 0.70 | 0.38 |
