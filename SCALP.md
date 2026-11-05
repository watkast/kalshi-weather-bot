# Range-Scalp Bot

*Updated Thu Nov 05 14:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48405 | 42175 | 6230 (73) | 3 | $-13788.88 | -4.5% |
| **+10¢** | 36137 | 28900 | 7237 (99) | 1 | $-12630.19 | -5.6% |
| **+15¢** | 30279 | 22485 | 7794 (127) | 2 | $-11530.46 | -6.1% |
| **+20¢** | 26902 | 18737 | 8165 (166) | 2 | $-10178.12 | -6.0% |
| **+10¢ (15¢ stop)** | 59012 | 58919 | 93 (56) | 0 | $-21939.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 14:28 | +10 stop | ZEC | DOWN | 0.36 | 0.63 | 2.40 |
| 11-05 14:28 | +10 stop | NEAR | DOWN | 0.68 | 0.51 | -2.04 |
| 11-05 14:27 | +10 stop | DOGE | UP | 0.70 | 0.53 | -2.03 |
| 11-05 14:27 | +10 stop | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 11-05 14:25 | +10 stop | XRP | UP | 0.69 | 0.80 | 0.83 |
| 11-05 14:25 | +5 | XRP | UP | 0.62 | 0.70 | 0.48 |
| 11-05 14:25 | +10 stop | HYPE | UP | 0.50 | 0.68 | 1.46 |
| 11-05 14:25 | +10 stop | ETH | DOWN | 0.65 | 0.48 | -2.04 |
| 11-05 14:25 | +10 stop | DOGE | DOWN | 0.47 | 0.59 | 0.85 |
| 11-05 14:25 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 11-05 14:25 | +20 | SOL | UP | 0.66 | 0.88 | 1.96 |
| 11-05 14:25 | +15 | SOL | UP | 0.66 | 0.88 | 1.96 |
| 11-05 14:25 | +10 | SOL | UP | 0.66 | 0.76 | 0.71 |
| 11-05 14:25 | +5 | SOL | UP | 0.66 | 0.71 | 0.19 |
| 11-05 14:24 | +10 stop | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 11-05 14:24 | +10 stop | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 11-05 14:24 | +10 stop | XRP | UP | 0.65 | 0.49 | -1.94 |
| 11-05 14:24 | +5 | XRP | UP | 0.65 | 0.70 | 0.19 |
| 11-05 14:24 | +10 stop | NEAR | DOWN | 0.54 | 0.65 | 0.76 |
| 11-05 14:24 | +10 stop | HYPE | UP | 0.65 | 0.49 | -1.94 |
| 11-05 14:24 | +10 | HYPE | UP | 0.65 | 0.81 | 1.33 |
| 11-05 14:24 | +10 stop | BNB | DOWN | 0.58 | 0.75 | 1.38 |
| 11-05 14:23 | +10 stop | DOGE | UP | 0.70 | 0.39 | -3.42 |
| 11-05 14:22 | +10 stop | ETH | DOWN | 0.55 | 0.70 | 1.17 |
| 11-05 14:22 | +10 stop | DOGE | UP | 0.63 | 0.76 | 1.00 |
| 11-05 14:22 | +10 stop | XRP | UP | 0.65 | 0.80 | 1.22 |
| 11-05 14:20 | +10 stop | XRP | DOWN | 0.60 | 0.40 | -2.34 |
| 11-05 14:20 | +10 stop | DOGE | DOWN | 0.59 | 0.34 | -2.83 |
| 11-05 14:20 | +5 | DOGE | DOWN | 0.59 | open |  |
| 11-05 14:20 | +10 stop | BNB | DOWN | 0.63 | 0.40 | -2.61 |
| 11-05 14:20 | +10 stop | BTC | DOWN | 0.71 | 0.56 | -1.83 |
| 11-05 14:20 | +10 stop | NEAR | DOWN | 0.58 | 0.36 | -2.55 |
| 11-05 14:20 | +10 stop | ETH | DOWN | 0.65 | 0.50 | -1.84 |
| 11-05 14:20 | +5 | HYPE | DOWN | 0.57 | open |  |
| 11-05 14:20 | +10 stop | SOL | UP | 0.61 | 0.74 | 0.99 |
| 11-05 14:20 | +20 | SOL | UP | 0.61 | 0.83 | 1.93 |
| 11-05 14:20 | +15 | SOL | UP | 0.61 | 0.77 | 1.30 |
| 11-05 14:20 | +10 | SOL | UP | 0.61 | 0.74 | 0.99 |
| 11-05 14:20 | +5 | SOL | UP | 0.61 | 0.70 | 0.58 |
| 11-05 14:20 | +5 | DOGE | UP | 0.44 | 0.53 | 0.54 |
