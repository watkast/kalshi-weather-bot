# Range-Scalp Bot

*Updated Sat Oct 17 15:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21145 | 18403 | 2742 (29) | 1 | $-6172.30 | -4.6% |
| **+10¢** | 15919 | 12754 | 3165 (41) | 1 | $-5495.84 | -5.5% |
| **+15¢** | 13306 | 9897 | 3409 (61) | 3 | $-4994.66 | -6.0% |
| **+20¢** | 11793 | 8222 | 3571 (80) | 4 | $-4427.21 | -6.0% |
| **+10¢ (15¢ stop)** | 25976 | 25926 | 50 (29) | 0 | $-9868.97 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 15:02 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-17 15:02 | +20 | BTC | DOWN | 0.61 | open |  |
| 10-17 15:02 | +15 | BTC | DOWN | 0.61 | open |  |
| 10-17 15:02 | +10 | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-17 15:02 | +5 | BTC | DOWN | 0.61 | 0.68 | 0.37 |
| 10-17 15:01 | +10 stop | HYPE | UP | 0.54 | 0.33 | -2.44 |
| 10-17 15:01 | +20 | HYPE | UP | 0.54 | open |  |
| 10-17 15:01 | +15 | HYPE | UP | 0.54 | open |  |
| 10-17 15:01 | +10 | HYPE | UP | 0.54 | open |  |
| 10-17 15:01 | +5 | HYPE | UP | 0.54 | open |  |
| 10-17 15:01 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-17 15:01 | +20 | ZEC | DOWN | 0.71 | open |  |
| 10-17 15:01 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-17 15:01 | +20 | DOGE | DOWN | 0.64 | 0.85 | 1.84 |
| 10-17 15:01 | +15 | DOGE | DOWN | 0.64 | 0.85 | 1.84 |
| 10-17 15:01 | +10 | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-17 15:01 | +5 | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-17 15:01 | +10 stop | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 10-17 15:01 | +20 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 10-17 15:01 | +15 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 10-17 15:01 | +10 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 10-17 15:01 | +5 | XRP | DOWN | 0.61 | 0.67 | 0.27 |
| 10-17 15:01 | +10 stop | BNB | DOWN | 0.71 | 0.84 | 1.05 |
| 10-17 15:01 | +20 | BNB | DOWN | 0.71 | open |  |
| 10-17 15:01 | +15 | BNB | DOWN | 0.71 | open |  |
| 10-17 15:01 | +10 | BNB | DOWN | 0.71 | 0.84 | 1.05 |
| 10-17 15:01 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
| 10-17 15:01 | +10 stop | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 10-17 15:01 | +20 | ETH | DOWN | 0.62 | 0.85 | 2.04 |
| 10-17 15:01 | +15 | ETH | DOWN | 0.62 | 0.85 | 2.04 |
| 10-17 15:01 | +10 | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 10-17 15:01 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 10-17 14:58 | +10 stop | BTC | DOWN | 0.63 | 0.79 | 1.31 |
| 10-17 14:57 | +10 stop | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-17 14:57 | +10 stop | BTC | UP | 0.57 | 0.41 | -1.95 |
| 10-17 14:55 | +10 stop | BTC | UP | 0.63 | 0.86 | 2.04 |
| 10-17 14:54 | +10 stop | DOGE | UP | 0.64 | 0.49 | -1.85 |
| 10-17 14:53 | +10 stop | XRP | UP | 0.69 | 0.83 | 1.15 |
| 10-17 14:53 | +5 | XRP | UP | 0.69 | 0.74 | 0.21 |
| 10-17 14:53 | +10 stop | ETH | UP | 0.71 | 0.90 | 1.69 |
