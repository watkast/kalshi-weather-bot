# Range-Scalp Bot

*Updated Sun Nov 15 05:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60430 | 52710 | 7720 (107) | 1 | $-16462.50 | -4.3% |
| **+10¢** | 45146 | 36101 | 9045 (143) | 2 | $-15540.97 | -5.5% |
| **+15¢** | 37812 | 28058 | 9754 (181) | 4 | $-14213.96 | -6.0% |
| **+20¢** | 33703 | 23471 | 10232 (233) | 5 | $-12511.26 | -5.9% |
| **+10¢ (15¢ stop)** | 73577 | 73434 | 143 (82) | 0 | $-27105.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 05:25 | +5 | ZEC | UP | 0.25 | 0.56 | 2.78 |
| 11-15 05:24 | +10 stop | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 11-15 05:24 | +10 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 11-15 05:23 | +5 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-15 05:23 | +10 stop | XRP | DOWN | 0.52 | 0.63 | 0.75 |
| 11-15 05:23 | +10 | XRP | DOWN | 0.52 | 0.63 | 0.75 |
| 11-15 05:23 | +5 | XRP | DOWN | 0.52 | 0.61 | 0.55 |
| 11-15 05:22 | +5 | ETH | UP | 0.63 | open |  |
| 11-15 05:21 | +5 | ETH | UP | 0.53 | 0.60 | 0.35 |
| 11-15 05:21 | +10 stop | ZEC | UP | 0.70 | 0.25 | -4.79 |
| 11-15 05:21 | +10 | ZEC | UP | 0.71 | open |  |
| 11-15 05:21 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 11-15 05:20 | +10 stop | BTC | UP | 0.66 | 0.79 | 1.02 |
| 11-15 05:20 | +10 | BTC | UP | 0.66 | 0.79 | 1.02 |
| 11-15 05:20 | +5 | BTC | UP | 0.66 | 0.71 | 0.19 |
| 11-15 05:20 | +10 stop | XRP | UP | 0.48 | 0.64 | 1.25 |
| 11-15 05:20 | +10 | XRP | UP | 0.48 | 0.64 | 1.25 |
| 11-15 05:20 | +5 | XRP | UP | 0.48 | 0.64 | 1.25 |
| 11-15 05:20 | +10 stop | HYPE | UP | 0.69 | 0.80 | 0.81 |
| 11-15 05:20 | +15 | HYPE | UP | 0.69 | 0.86 | 1.44 |
| 11-15 05:20 | +10 | HYPE | UP | 0.69 | 0.80 | 0.81 |
| 11-15 05:20 | +20 | HYPE | UP | 0.71 | open |  |
| 11-15 05:20 | +5 | HYPE | UP | 0.70 | 0.75 | 0.23 |
| 11-15 05:20 | +10 stop | ETH | UP | 0.54 | 0.30 | -2.73 |
| 11-15 05:20 | +5 | ETH | UP | 0.55 | 0.60 | 0.15 |
| 11-15 05:18 | +10 stop | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-15 05:18 | +20 | XRP | UP | 0.67 | open |  |
| 11-15 05:18 | +15 | XRP | UP | 0.66 | open |  |
| 11-15 05:18 | +10 | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-15 05:18 | +5 | XRP | UP | 0.67 | 0.74 | 0.40 |
| 11-15 05:18 | +5 | NEAR | UP | 0.67 | 0.72 | 0.19 |
| 11-15 05:17 | +5 | HYPE | UP | 0.68 | 0.75 | 0.40 |
| 11-15 05:17 | +10 stop | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 11-15 05:17 | +20 | ZEC | UP | 0.64 | open |  |
| 11-15 05:17 | +15 | ZEC | UP | 0.64 | open |  |
| 11-15 05:17 | +10 | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 11-15 05:17 | +5 | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 11-15 05:17 | +10 stop | NEAR | UP | 0.65 | 0.81 | 1.33 |
| 11-15 05:17 | +20 | NEAR | UP | 0.65 | 0.86 | 1.85 |
| 11-15 05:17 | +15 | NEAR | UP | 0.65 | 0.81 | 1.33 |
