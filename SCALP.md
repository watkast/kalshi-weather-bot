# Range-Scalp Bot

*Updated Sat Nov 21 22:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67846 | 59220 | 8626 (138) | 5 | $-18139.65 | -4.2% |
| **+10¢** | 50656 | 40577 | 10079 (181) | 6 | $-16815.36 | -5.3% |
| **+15¢** | 42465 | 31601 | 10864 (230) | 6 | $-15052.36 | -5.7% |
| **+20¢** | 37801 | 26383 | 11418 (288) | 7 | $-13373.02 | -5.6% |
| **+10¢ (15¢ stop)** | 82588 | 82410 | 178 (110) | 1 | $-30310.73 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 22:25 | +10 stop | XRP | UP | 0.70 | open |  |
| 11-21 22:22 | +10 stop | BTC | UP | 0.55 | 0.40 | -1.85 |
| 11-21 22:20 | +10 stop | HYPE | UP | 0.61 | 0.77 | 1.30 |
| 11-21 22:19 | +5 | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-21 22:19 | +10 stop | XRP | UP | 0.59 | 0.73 | 1.09 |
| 11-21 22:18 | +10 stop | ETH | UP | 0.55 | 0.67 | 0.86 |
| 11-21 22:18 | +5 | DOGE | UP | 0.59 | 0.69 | 0.68 |
| 11-21 22:17 | +10 stop | BTC | DOWN | 0.60 | 0.45 | -1.85 |
| 11-21 22:17 | +20 | BTC | DOWN | 0.60 | open |  |
| 11-21 22:17 | +15 | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 11-21 22:17 | +10 | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 11-21 22:17 | +5 | BTC | DOWN | 0.60 | 0.65 | 0.17 |
| 11-21 22:17 | +10 stop | HYPE | UP | 0.55 | 0.69 | 1.12 |
| 11-21 22:17 | +10 stop | DOGE | UP | 0.53 | 0.69 | 1.27 |
| 11-21 22:17 | +20 | DOGE | UP | 0.53 | 0.74 | 1.78 |
| 11-21 22:17 | +15 | DOGE | UP | 0.53 | 0.69 | 1.27 |
| 11-21 22:17 | +10 | DOGE | UP | 0.53 | 0.69 | 1.27 |
| 11-21 22:17 | +5 | DOGE | UP | 0.53 | 0.62 | 0.55 |
| 11-21 22:17 | +5 | ZEC | UP | 0.67 | 0.77 | 0.71 |
| 11-21 22:16 | +10 stop | BNB | DOWN | 0.52 | 0.30 | -2.53 |
| 11-21 22:16 | +20 | BNB | DOWN | 0.52 | open |  |
| 11-21 22:16 | +15 | BNB | DOWN | 0.52 | open |  |
| 11-21 22:16 | +10 | BNB | DOWN | 0.52 | open |  |
| 11-21 22:16 | +5 | BNB | DOWN | 0.52 | open |  |
| 11-21 22:16 | +10 stop | NEAR | UP | 0.58 | 0.70 | 0.83 |
| 11-21 22:16 | +20 | NEAR | UP | 0.58 | 0.88 | 2.70 |
| 11-21 22:16 | +15 | NEAR | UP | 0.58 | 0.74 | 1.24 |
| 11-21 22:16 | +10 | NEAR | UP | 0.58 | 0.70 | 0.83 |
| 11-21 22:16 | +5 | NEAR | UP | 0.58 | 0.65 | 0.32 |
| 11-21 22:16 | +10 stop | XRP | DOWN | 0.55 | 0.36 | -2.25 |
| 11-21 22:16 | +20 | XRP | DOWN | 0.55 | open |  |
| 11-21 22:16 | +15 | XRP | DOWN | 0.55 | open |  |
| 11-21 22:16 | +10 | XRP | DOWN | 0.55 | open |  |
| 11-21 22:16 | +5 | XRP | DOWN | 0.55 | open |  |
| 11-21 22:16 | +10 stop | ZEC | DOWN | 0.49 | 0.34 | -1.84 |
| 11-21 22:16 | +20 | ZEC | DOWN | 0.49 | open |  |
| 11-21 22:16 | +15 | ZEC | DOWN | 0.49 | open |  |
| 11-21 22:16 | +10 | ZEC | DOWN | 0.49 | open |  |
| 11-21 22:16 | +5 | ZEC | DOWN | 0.49 | 0.58 | 0.54 |
| 11-21 22:16 | +10 stop | HYPE | DOWN | 0.62 | 0.45 | -2.05 |
