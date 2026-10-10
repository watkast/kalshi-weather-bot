# Range-Scalp Bot

*Updated Sat Oct 10 04:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9954 | 8594 | 1360 (18) | 6 | $-3331.57 | -5.3% |
| **+10¢** | 7519 | 5933 | 1586 (30) | 7 | $-3200.46 | -6.8% |
| **+15¢** | 6348 | 4675 | 1673 (43) | 7 | $-2638.14 | -6.6% |
| **+20¢** | 5641 | 3903 | 1738 (55) | 7 | $-2199.27 | -6.2% |
| **+10¢ (15¢ stop)** | 12230 | 12195 | 35 (22) | 1 | $-4795.87 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 04:39 | +10 stop | XRP | UP | 0.67 | open |  |
| 10-10 04:39 | +10 stop | BTC | DOWN | 0.41 | 0.54 | 0.95 |
| 10-10 04:39 | +5 | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 10-10 04:39 | +10 stop | ZEC | DOWN | 0.62 | 0.36 | -2.94 |
| 10-10 04:39 | +5 | DOGE | UP | 0.61 | 0.66 | 0.21 |
| 10-10 04:38 | +10 stop | DOGE | UP | 0.61 | 0.74 | 0.99 |
| 10-10 04:38 | +5 | DOGE | UP | 0.61 | 0.66 | 0.17 |
| 10-10 04:37 | +10 stop | SOL | DOWN | 0.35 | 0.56 | 1.76 |
| 10-10 04:37 | +10 stop | ZEC | UP | 0.60 | 0.43 | -2.05 |
| 10-10 04:37 | +10 stop | DOGE | DOWN | 0.57 | 0.69 | 0.87 |
| 10-10 04:37 | +5 | DOGE | DOWN | 0.57 | 0.69 | 0.87 |
| 10-10 04:37 | +10 stop | BTC | DOWN | 0.68 | 0.50 | -2.14 |
| 10-10 04:37 | +10 stop | XRP | DOWN | 0.55 | 0.13 | -4.46 |
| 10-10 04:36 | +10 stop | SOL | UP | 0.61 | 0.45 | -1.95 |
| 10-10 04:35 | +10 stop | HYPE | UP | 0.64 | 0.86 | 1.94 |
| 10-10 04:33 | +10 stop | BNB | UP | 0.56 | 0.72 | 1.27 |
| 10-10 04:33 | +20 | BNB | UP | 0.56 | 0.77 | 1.79 |
| 10-10 04:33 | +15 | BNB | UP | 0.56 | 0.72 | 1.27 |
| 10-10 04:33 | +10 | BNB | UP | 0.56 | 0.72 | 1.27 |
| 10-10 04:33 | +5 | BNB | UP | 0.56 | 0.72 | 1.27 |
| 10-10 04:33 | +10 stop | NEAR | DOWN | 0.69 | 0.53 | -1.92 |
| 10-10 04:33 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-10 04:33 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-10 04:33 | +10 stop | XRP | DOWN | 0.69 | 0.50 | -2.23 |
| 10-10 04:33 | +20 | XRP | DOWN | 0.69 | open |  |
| 10-10 04:33 | +15 | XRP | DOWN | 0.69 | open |  |
| 10-10 04:33 | +10 | XRP | DOWN | 0.69 | open |  |
| 10-10 04:33 | +5 | XRP | DOWN | 0.69 | open |  |
| 10-10 04:32 | +5 | SOL | DOWN | 0.70 | open |  |
| 10-10 04:31 | +10 stop | ZEC | DOWN | 0.69 | 0.50 | -2.28 |
| 10-10 04:31 | +20 | ZEC | DOWN | 0.69 | open |  |
| 10-10 04:31 | +15 | ZEC | DOWN | 0.70 | open |  |
| 10-10 04:31 | +10 | ZEC | DOWN | 0.70 | open |  |
| 10-10 04:31 | +5 | ZEC | DOWN | 0.70 | open |  |
| 10-10 04:31 | +10 stop | HYPE | DOWN | 0.67 | 0.44 | -2.68 |
| 10-10 04:31 | +20 | HYPE | DOWN | 0.67 | open |  |
| 10-10 04:31 | +15 | HYPE | DOWN | 0.67 | open |  |
| 10-10 04:31 | +10 | HYPE | DOWN | 0.67 | open |  |
| 10-10 04:31 | +5 | HYPE | DOWN | 0.67 | open |  |
| 10-10 04:31 | +10 stop | BTC | DOWN | 0.67 | 0.43 | -2.74 |
