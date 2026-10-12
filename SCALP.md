# Range-Scalp Bot

*Updated Mon Oct 12 03:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12974 | 11201 | 1773 (25) | 2 | $-4277.34 | -5.2% |
| **+10¢** | 9840 | 7792 | 2048 (37) | 3 | $-3981.38 | -6.4% |
| **+15¢** | 8271 | 6086 | 2185 (55) | 4 | $-3489.34 | -6.7% |
| **+20¢** | 7364 | 5088 | 2276 (69) | 5 | $-2975.02 | -6.4% |
| **+10¢ (15¢ stop)** | 16004 | 15963 | 41 (25) | 1 | $-6318.20 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 03:26 | +10 stop | XRP | DOWN | 0.69 | open |  |
| 10-12 03:25 | +5 | XRP | DOWN | 0.65 | open |  |
| 10-12 03:25 | +10 stop | ETH | DOWN | 0.70 | 0.51 | -2.23 |
| 10-12 03:25 | +15 | ETH | DOWN | 0.70 | open |  |
| 10-12 03:25 | +10 | ETH | DOWN | 0.70 | open |  |
| 10-12 03:25 | +5 | ETH | DOWN | 0.70 | 0.79 | 0.63 |
| 10-12 03:25 | +10 stop | XRP | DOWN | 0.62 | 0.43 | -2.25 |
| 10-12 03:24 | +5 | HYPE | UP | 0.64 | 0.72 | 0.44 |
| 10-12 03:23 | +10 stop | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 10-12 03:23 | +15 | SOL | DOWN | 0.58 | 0.74 | 1.28 |
| 10-12 03:23 | +10 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 10-12 03:23 | +5 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 10-12 03:23 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 03:23 | +10 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 03:23 | +5 | BTC | DOWN | 0.64 | 0.73 | 0.59 |
| 10-12 03:23 | +10 stop | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 10-12 03:23 | +10 | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 10-12 03:23 | +5 | ZEC | UP | 0.70 | 0.76 | 0.32 |
| 10-12 03:23 | +10 stop | HYPE | UP | 0.63 | 0.75 | 0.89 |
| 10-12 03:23 | +10 | HYPE | UP | 0.63 | 0.75 | 0.89 |
| 10-12 03:23 | +5 | HYPE | UP | 0.63 | 0.70 | 0.38 |
| 10-12 03:23 | +10 stop | XRP | DOWN | 0.60 | 0.44 | -1.95 |
| 10-12 03:23 | +5 | XRP | DOWN | 0.60 | 0.66 | 0.27 |
| 10-12 03:23 | +10 stop | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-12 03:23 | +20 | DOGE | UP | 0.70 | 0.90 | 1.79 |
| 10-12 03:23 | +15 | DOGE | UP | 0.70 | 0.85 | 1.26 |
| 10-12 03:23 | +10 | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-12 03:23 | +5 | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-12 03:23 | +10 stop | ETH | DOWN | 0.53 | 0.68 | 1.16 |
| 10-12 03:23 | +15 | ETH | DOWN | 0.53 | 0.68 | 1.16 |
| 10-12 03:23 | +10 | ETH | DOWN | 0.53 | 0.68 | 1.16 |
| 10-12 03:23 | +5 | ETH | DOWN | 0.53 | 0.60 | 0.35 |
| 10-12 03:22 | +10 | BTC | UP | 0.51 | 0.62 | 0.75 |
| 10-12 03:22 | +5 | BTC | UP | 0.51 | 0.58 | 0.34 |
| 10-12 03:21 | +10 stop | BTC | UP | 0.67 | 0.50 | -2.04 |
| 10-12 03:21 | +10 stop | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 10-12 03:20 | +10 stop | ETH | UP | 0.64 | 0.79 | 1.21 |
| 10-12 03:20 | +10 stop | BTC | DOWN | 0.62 | 0.45 | -2.05 |
| 10-12 03:20 | +10 stop | SOL | DOWN | 0.52 | 0.32 | -2.37 |
| 10-12 03:20 | +10 stop | DOGE | UP | 0.68 | 0.85 | 1.45 |
