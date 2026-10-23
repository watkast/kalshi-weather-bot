# Range-Scalp Bot

*Updated Fri Oct 23 10:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30170 | 26269 | 3901 (39) | 2 | $-8856.13 | -4.7% |
| **+10¢** | 22617 | 18102 | 4515 (56) | 0 | $-7942.24 | -5.6% |
| **+15¢** | 18931 | 14075 | 4856 (79) | 0 | $-7185.00 | -6.0% |
| **+20¢** | 16756 | 11669 | 5087 (102) | 0 | $-6486.84 | -6.2% |
| **+10¢ (15¢ stop)** | 37001 | 36942 | 59 (32) | 0 | $-13943.74 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 10:25 | +10 stop | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-23 10:25 | +15 | BTC | DOWN | 0.68 | 0.86 | 1.55 |
| 10-23 10:25 | +10 | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-23 10:24 | +10 stop | ZEC | DOWN | 0.70 | 0.91 | 1.88 |
| 10-23 10:24 | +10 | ZEC | DOWN | 0.70 | 0.91 | 1.88 |
| 10-23 10:24 | +5 | ZEC | DOWN | 0.70 | 0.91 | 1.88 |
| 10-23 10:23 | +10 stop | ETH | UP | 0.68 | 0.46 | -2.54 |
| 10-23 10:23 | +5 | ETH | UP | 0.68 | open |  |
| 10-23 10:22 | +5 | BNB | DOWN | 0.63 | 0.72 | 0.58 |
| 10-23 10:22 | +10 stop | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-23 10:22 | +10 stop | DOGE | UP | 0.60 | 0.39 | -2.44 |
| 10-23 10:22 | +5 | DOGE | UP | 0.60 | 0.68 | 0.47 |
| 10-23 10:22 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-23 10:21 | +10 stop | ZEC | UP | 0.58 | 0.33 | -2.84 |
| 10-23 10:21 | +10 stop | XRP | UP | 0.60 | 0.45 | -1.85 |
| 10-23 10:21 | +10 stop | HYPE | UP | 0.61 | 0.39 | -2.54 |
| 10-23 10:20 | +10 stop | BTC | UP | 0.69 | 0.47 | -2.53 |
| 10-23 10:20 | +5 | BTC | UP | 0.70 | open |  |
| 10-23 10:20 | +10 stop | ZEC | DOWN | 0.57 | 0.37 | -2.35 |
| 10-23 10:20 | +15 | ZEC | DOWN | 0.58 | 0.74 | 1.29 |
| 10-23 10:20 | +10 | ZEC | DOWN | 0.58 | 0.69 | 0.77 |
| 10-23 10:20 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.36 |
| 10-23 10:20 | +5 | DOGE | UP | 0.59 | 0.69 | 0.68 |
| 10-23 10:20 | +5 | DOGE | DOWN | 0.45 | 0.60 | 1.15 |
| 10-23 10:19 | +5 | XRP | DOWN | 0.61 | 0.72 | 0.73 |
| 10-23 10:19 | +5 | BTC | UP | 0.56 | 0.62 | 0.25 |
| 10-23 10:19 | +5 | SOL | DOWN | 0.60 | 0.78 | 1.50 |
| 10-23 10:18 | +10 stop | BNB | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 10:18 | +15 | BNB | DOWN | 0.59 | 0.79 | 1.71 |
| 10-23 10:18 | +10 | BNB | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 10:18 | +5 | BNB | DOWN | 0.59 | 0.65 | 0.27 |
| 10-23 10:18 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-23 10:18 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 10-23 10:18 | +5 | HYPE | DOWN | 0.60 | 0.65 | 0.17 |
| 10-23 10:18 | +10 stop | BNB | DOWN | 0.52 | 0.67 | 1.16 |
| 10-23 10:18 | +20 | BNB | DOWN | 0.52 | 0.72 | 1.67 |
| 10-23 10:18 | +15 | BNB | DOWN | 0.52 | 0.67 | 1.16 |
| 10-23 10:18 | +10 | BNB | DOWN | 0.52 | 0.67 | 1.16 |
| 10-23 10:18 | +5 | BNB | DOWN | 0.52 | 0.67 | 1.16 |
| 10-23 10:18 | +5 | SOL | DOWN | 0.53 | 0.62 | 0.55 |
