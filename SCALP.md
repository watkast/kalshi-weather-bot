# Range-Scalp Bot

*Updated Sat Oct 24 11:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31939 | 27847 | 4092 (40) | 9 | $-9133.76 | -4.5% |
| **+10¢** | 23890 | 19157 | 4733 (58) | 9 | $-8151.77 | -5.4% |
| **+15¢** | 19996 | 14908 | 5088 (81) | 9 | $-7282.83 | -5.8% |
| **+20¢** | 17712 | 12385 | 5327 (103) | 9 | $-6473.95 | -5.8% |
| **+10¢ (15¢ stop)** | 39238 | 39179 | 59 (32) | 0 | $-14990.27 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 11:23 | +10 stop | DOGE | DOWN | 0.57 | 0.77 | 1.69 |
| 10-24 11:23 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-24 11:22 | +10 stop | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-24 11:22 | +10 | XRP | UP | 0.57 | open |  |
| 10-24 11:22 | +5 | XRP | UP | 0.63 | open |  |
| 10-24 11:22 | +10 | XRP | UP | 0.52 | 0.62 | 0.65 |
| 10-24 11:21 | +10 stop | DOGE | UP | 0.66 | 0.46 | -2.34 |
| 10-24 11:21 | +10 | DOGE | UP | 0.66 | open |  |
| 10-24 11:21 | +5 | DOGE | UP | 0.66 | open |  |
| 10-24 11:19 | +10 stop | BNB | UP | 0.59 | 0.42 | -2.05 |
| 10-24 11:19 | +10 stop | XRP | UP | 0.57 | 0.11 | -4.85 |
| 10-24 11:19 | +5 | XRP | UP | 0.57 | 0.62 | 0.15 |
| 10-24 11:19 | +10 stop | SOL | DOWN | 0.65 | 0.77 | 0.87 |
| 10-24 11:19 | +10 stop | XRP | DOWN | 0.45 | 0.62 | 1.35 |
| 10-24 11:19 | +5 | XRP | DOWN | 0.45 | 0.62 | 1.35 |
| 10-24 11:19 | +10 stop | NEAR | DOWN | 0.57 | 0.84 | 2.43 |
| 10-24 11:19 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-24 11:18 | +10 stop | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 10-24 11:18 | +5 | XRP | DOWN | 0.59 | 0.64 | 0.16 |
| 10-24 11:18 | +10 stop | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-24 11:18 | +10 stop | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-24 11:18 | +10 stop | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-24 11:17 | +5 | XRP | DOWN | 0.56 | 0.63 | 0.35 |
| 10-24 11:16 | +10 stop | ZEC | UP | 0.63 | 0.44 | -2.25 |
| 10-24 11:16 | +20 | ZEC | UP | 0.63 | open |  |
| 10-24 11:16 | +15 | ZEC | UP | 0.63 | open |  |
| 10-24 11:16 | +10 | ZEC | UP | 0.63 | open |  |
| 10-24 11:16 | +5 | ZEC | UP | 0.63 | open |  |
| 10-24 11:16 | +10 stop | BNB | UP | 0.64 | 0.47 | -2.09 |
| 10-24 11:16 | +10 stop | ETH | UP | 0.56 | 0.33 | -2.64 |
| 10-24 11:16 | +20 | ETH | UP | 0.56 | open |  |
| 10-24 11:16 | +15 | ETH | UP | 0.56 | open |  |
| 10-24 11:16 | +10 | ETH | UP | 0.56 | open |  |
| 10-24 11:16 | +5 | ETH | UP | 0.56 | open |  |
| 10-24 11:16 | +10 stop | NEAR | UP | 0.55 | 0.35 | -2.34 |
| 10-24 11:16 | +20 | NEAR | UP | 0.55 | open |  |
| 10-24 11:16 | +15 | NEAR | UP | 0.55 | open |  |
| 10-24 11:16 | +10 | NEAR | UP | 0.55 | open |  |
| 10-24 11:16 | +5 | NEAR | UP | 0.55 | open |  |
| 10-24 11:16 | +10 stop | DOGE | UP | 0.56 | 0.67 | 0.76 |
