# Range-Scalp Bot

*Updated Tue Nov 24 06:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70520 | 61558 | 8962 (148) | 2 | $-18814.42 | -4.2% |
| **+10¢** | 52612 | 42148 | 10464 (192) | 1 | $-17409.87 | -5.3% |
| **+15¢** | 44073 | 32802 | 11271 (248) | 0 | $-15487.67 | -5.6% |
| **+20¢** | 39249 | 27383 | 11866 (314) | 0 | $-13843.08 | -5.6% |
| **+10¢ (15¢ stop)** | 85861 | 85663 | 198 (118) | 0 | $-31559.02 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 06:21 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.39 |
| 11-24 06:21 | +10 stop | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 11-24 06:21 | +5 | ZEC | DOWN | 0.59 | 0.66 | 0.37 |
| 11-24 06:20 | +10 stop | XRP | UP | 0.58 | 0.24 | -3.68 |
| 11-24 06:20 | +10 stop | BNB | UP | 0.65 | 0.47 | -2.14 |
| 11-24 06:20 | +10 stop | NEAR | DOWN | 0.68 | 0.84 | 1.34 |
| 11-24 06:20 | +5 | NEAR | DOWN | 0.67 | 0.75 | 0.46 |
| 11-24 06:20 | +10 stop | HYPE | UP | 0.55 | 0.40 | -1.85 |
| 11-24 06:20 | +5 | HYPE | UP | 0.55 | open |  |
| 11-24 06:20 | +10 stop | SOL | UP | 0.68 | 0.37 | -3.43 |
| 11-24 06:20 | +10 | SOL | UP | 0.68 | open |  |
| 11-24 06:20 | +5 | SOL | UP | 0.68 | open |  |
| 11-24 06:20 | +10 stop | ZEC | DOWN | 0.59 | 0.86 | 2.44 |
| 11-24 06:20 | +10 | ZEC | DOWN | 0.59 | 0.86 | 2.47 |
| 11-24 06:20 | +5 | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-24 06:19 | +10 stop | ETH | UP | 0.67 | 0.84 | 1.44 |
| 11-24 06:19 | +5 | ETH | UP | 0.66 | 0.84 | 1.54 |
| 11-24 06:19 | +10 stop | BTC | UP | 0.60 | 0.70 | 0.68 |
| 11-24 06:19 | +5 | BTC | UP | 0.60 | 0.70 | 0.68 |
| 11-24 06:19 | +10 stop | HYPE | DOWN | 0.60 | 0.71 | 0.78 |
| 11-24 06:19 | +5 | HYPE | DOWN | 0.60 | 0.67 | 0.36 |
| 11-24 06:18 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-24 06:18 | +10 | NEAR | DOWN | 0.68 | 0.84 | 1.32 |
| 11-24 06:18 | +5 | NEAR | DOWN | 0.68 | 0.77 | 0.61 |
| 11-24 06:18 | +10 stop | BNB | DOWN | 0.69 | 0.53 | -1.93 |
| 11-24 06:18 | +10 | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-24 06:18 | +5 | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 11-24 06:18 | +10 stop | XRP | DOWN | 0.67 | 0.43 | -2.74 |
| 11-24 06:18 | +10 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-24 06:18 | +5 | XRP | DOWN | 0.67 | 0.74 | 0.40 |
| 11-24 06:18 | +5 | BTC | DOWN | 0.42 | 0.51 | 0.54 |
| 11-24 06:18 | +5 | ZEC | DOWN | 0.47 | 0.53 | 0.24 |
| 11-24 06:18 | +10 stop | SOL | DOWN | 0.47 | 0.57 | 0.64 |
| 11-24 06:18 | +10 | SOL | DOWN | 0.46 | 0.56 | 0.64 |
| 11-24 06:18 | +5 | SOL | DOWN | 0.46 | 0.56 | 0.64 |
| 11-24 06:18 | +5 | ETH | DOWN | 0.41 | 0.46 | 0.15 |
| 11-24 06:16 | +10 stop | DOGE | DOWN | 0.69 | 0.83 | 1.15 |
| 11-24 06:16 | +20 | DOGE | DOWN | 0.69 | 0.90 | 1.91 |
| 11-24 06:16 | +15 | DOGE | DOWN | 0.69 | 0.90 | 1.91 |
| 11-24 06:16 | +10 | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
