# Range-Scalp Bot

*Updated Sat Oct 17 22:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21692 | 18908 | 2784 (29) | 1 | $-6148.84 | -4.5% |
| **+10¢** | 16319 | 13099 | 3220 (41) | 1 | $-5466.18 | -5.3% |
| **+15¢** | 13645 | 10170 | 3475 (61) | 2 | $-4965.86 | -5.8% |
| **+20¢** | 12084 | 8442 | 3642 (80) | 3 | $-4417.65 | -5.8% |
| **+10¢ (15¢ stop)** | 26641 | 26591 | 50 (29) | 0 | $-10134.23 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 22:55 | +10 stop | HYPE | UP | 0.63 | 0.83 | 1.73 |
| 10-17 22:53 | +10 stop | HYPE | DOWN | 0.62 | 0.36 | -2.94 |
| 10-17 22:53 | +10 stop | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-17 22:53 | +20 | ZEC | UP | 0.67 | 0.87 | 1.76 |
| 10-17 22:53 | +15 | ZEC | UP | 0.67 | 0.85 | 1.55 |
| 10-17 22:53 | +10 | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-17 22:53 | +5 | ZEC | UP | 0.67 | 0.74 | 0.40 |
| 10-17 22:53 | +10 stop | NEAR | DOWN | 0.63 | 0.81 | 1.55 |
| 10-17 22:53 | +10 stop | BTC | UP | 0.52 | 0.33 | -2.24 |
| 10-17 22:52 | +10 stop | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-17 22:52 | +10 | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-17 22:52 | +5 | ETH | UP | 0.67 | 0.74 | 0.40 |
| 10-17 22:51 | +10 stop | NEAR | UP | 0.66 | 0.46 | -2.34 |
| 10-17 22:51 | +15 | NEAR | UP | 0.66 | open |  |
| 10-17 22:51 | +5 | NEAR | UP | 0.66 | open |  |
| 10-17 22:48 | +10 | NEAR | UP | 0.70 | open |  |
| 10-17 22:48 | +10 stop | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 10-17 22:48 | +10 | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 10-17 22:48 | +5 | DOGE | UP | 0.71 | 0.77 | 0.32 |
| 10-17 22:48 | +5 | XRP | UP | 0.69 | 0.78 | 0.62 |
| 10-17 22:48 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 10-17 22:48 | +10 stop | HYPE | UP | 0.69 | 0.53 | -1.97 |
| 10-17 22:48 | +10 | HYPE | UP | 0.69 | 0.83 | 1.11 |
| 10-17 22:48 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 10-17 22:47 | +5 | HYPE | UP | 0.70 | 0.83 | 1.01 |
| 10-17 22:47 | +10 stop | BTC | UP | 0.71 | 0.52 | -2.23 |
| 10-17 22:47 | +10 stop | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-17 22:47 | +20 | DOGE | UP | 0.62 | 0.86 | 2.14 |
| 10-17 22:47 | +15 | DOGE | UP | 0.62 | 0.77 | 1.20 |
| 10-17 22:47 | +10 | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-17 22:47 | +5 | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-17 22:47 | +10 stop | ETH | UP | 0.63 | 0.76 | 1.00 |
| 10-17 22:47 | +20 | ETH | UP | 0.63 | 0.95 | 2.98 |
| 10-17 22:47 | +15 | ETH | UP | 0.63 | 0.79 | 1.31 |
| 10-17 22:47 | +10 | ETH | UP | 0.63 | 0.76 | 1.00 |
| 10-17 22:47 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 10-17 22:47 | +10 stop | XRP | UP | 0.64 | 0.78 | 1.10 |
| 10-17 22:47 | +20 | XRP | UP | 0.64 | open |  |
| 10-17 22:47 | +15 | XRP | UP | 0.64 | open |  |
| 10-17 22:47 | +10 | XRP | UP | 0.64 | 0.78 | 1.10 |
