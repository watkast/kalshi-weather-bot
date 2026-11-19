# Range-Scalp Bot

*Updated Thu Nov 19 23:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65465 | 57145 | 8320 (124) | 2 | $-17536.19 | -4.3% |
| **+10¢** | 48884 | 39154 | 9730 (165) | 2 | $-16326.19 | -5.3% |
| **+15¢** | 40994 | 30498 | 10496 (211) | 3 | $-14696.96 | -5.7% |
| **+20¢** | 36499 | 25471 | 11028 (266) | 3 | $-13030.48 | -5.7% |
| **+10¢ (15¢ stop)** | 79703 | 79539 | 164 (98) | 2 | $-29342.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 23:22 | +10 stop | ZEC | DOWN | 0.66 | open |  |
| 11-19 23:22 | +10 stop | BTC | UP | 0.55 | open |  |
| 11-19 23:22 | +15 | BTC | UP | 0.55 | open |  |
| 11-19 23:22 | +10 | BTC | UP | 0.55 | open |  |
| 11-19 23:22 | +5 | BTC | UP | 0.56 | open |  |
| 11-19 23:20 | +10 stop | ZEC | UP | 0.61 | 0.45 | -1.95 |
| 11-19 23:20 | +10 | ZEC | UP | 0.61 | open |  |
| 11-19 23:20 | +5 | ZEC | UP | 0.61 | open |  |
| 11-19 23:16 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-19 23:16 | +20 | XRP | UP | 0.71 | open |  |
| 11-19 23:16 | +15 | XRP | UP | 0.70 | open |  |
| 11-19 23:16 | +10 | XRP | UP | 0.70 | 0.81 | 0.84 |
| 11-19 23:16 | +5 | XRP | UP | 0.70 | 0.77 | 0.42 |
| 11-19 23:16 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-19 23:16 | +20 | BTC | UP | 0.67 | open |  |
| 11-19 23:16 | +15 | BTC | UP | 0.67 | 0.83 | 1.34 |
| 11-19 23:16 | +10 | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-19 23:16 | +5 | BTC | UP | 0.67 | 0.73 | 0.30 |
| 11-19 23:16 | +20 | ZEC | UP | 0.71 | open |  |
| 11-19 23:16 | +15 | ZEC | UP | 0.71 | open |  |
| 11-19 23:16 | +10 | ZEC | UP | 0.71 | 0.82 | 0.84 |
| 11-19 23:16 | +5 | ZEC | UP | 0.70 | 0.78 | 0.52 |
| 11-19 23:09 | +10 stop | XRP | DOWN | 0.47 | 0.73 | 2.28 |
| 11-19 23:09 | +10 stop | XRP | UP | 0.39 | 0.54 | 1.15 |
| 11-19 23:07 | +10 stop | XRP | DOWN | 0.54 | 0.34 | -2.34 |
| 11-19 23:07 | +10 stop | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 11-19 23:06 | +10 stop | XRP | UP | 0.60 | 0.43 | -2.05 |
| 11-19 23:05 | +5 | SOL | DOWN | 0.60 | 0.69 | 0.58 |
| 11-19 23:05 | +10 stop | BNB | DOWN | 0.65 | 0.47 | -2.14 |
| 11-19 23:05 | +10 stop | DOGE | DOWN | 0.60 | 0.70 | 0.68 |
| 11-19 23:05 | +10 stop | XRP | DOWN | 0.50 | 0.34 | -1.95 |
| 11-19 23:04 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-19 23:04 | +10 stop | SOL | DOWN | 0.71 | 0.51 | -2.33 |
| 11-19 23:04 | +10 stop | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-19 23:04 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-19 23:03 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-19 23:03 | +5 | BTC | UP | 0.57 | no | -5.88 |
| 11-19 23:03 | +10 stop | BNB | UP | 0.63 | 0.47 | -1.97 |
| 11-19 23:03 | +20 | BNB | UP | 0.64 | no | -6.59 |
| 11-19 23:03 | +15 | BNB | UP | 0.64 | no | -6.59 |
