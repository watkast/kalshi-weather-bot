# Range-Scalp Bot

*Updated Mon Nov 23 01:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69367 | 60523 | 8844 (146) | 0 | $-18700.20 | -4.3% |
| **+10¢** | 51764 | 41432 | 10332 (189) | 1 | $-17392.84 | -5.3% |
| **+15¢** | 43382 | 32251 | 11131 (244) | 1 | $-15550.64 | -5.7% |
| **+20¢** | 38636 | 26935 | 11701 (305) | 1 | $-13852.53 | -5.7% |
| **+10¢ (15¢ stop)** | 84467 | 84277 | 190 (118) | 1 | $-31064.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 01:34 | +5 | HYPE | UP | 0.60 | 0.66 | 0.27 |
| 11-23 01:32 | +10 stop | HYPE | UP | 0.66 | open |  |
| 11-23 01:31 | +10 stop | HYPE | UP | 0.68 | 0.52 | -1.94 |
| 11-23 01:31 | +20 | HYPE | UP | 0.68 | open |  |
| 11-23 01:31 | +15 | HYPE | UP | 0.68 | open |  |
| 11-23 01:31 | +10 | HYPE | UP | 0.68 | open |  |
| 11-23 01:31 | +5 | HYPE | UP | 0.68 | 0.74 | 0.30 |
| 11-23 01:28 | +10 stop | ZEC | DOWN | 0.71 | 0.30 | -4.40 |
| 11-23 01:28 | +10 stop | ETH | DOWN | 0.46 | 0.56 | 0.64 |
| 11-23 01:27 | +10 stop | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 11-23 01:27 | +20 | ETH | DOWN | 0.70 | 0.92 | 2.00 |
| 11-23 01:27 | +15 | ETH | DOWN | 0.70 | 0.92 | 2.00 |
| 11-23 01:25 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-23 01:23 | +10 stop | ZEC | DOWN | 0.64 | 0.45 | -2.25 |
| 11-23 01:23 | +10 stop | SOL | DOWN | 0.69 | 0.83 | 1.15 |
| 11-23 01:23 | +10 stop | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 11-23 01:23 | +10 stop | ZEC | UP | 0.47 | 0.57 | 0.64 |
| 11-23 01:23 | +10 stop | DOGE | DOWN | 0.67 | 0.81 | 1.13 |
| 11-23 01:23 | +10 stop | XRP | DOWN | 0.71 | 0.84 | 1.05 |
| 11-23 01:23 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 11-23 01:23 | +10 stop | ETH | DOWN | 0.61 | 0.73 | 0.89 |
| 11-23 01:22 | +10 stop | SOL | DOWN | 0.71 | 0.49 | -2.53 |
| 11-23 01:22 | +10 stop | NEAR | DOWN | 0.65 | 0.48 | -2.04 |
| 11-23 01:21 | +10 stop | ETH | DOWN | 0.63 | 0.75 | 0.89 |
| 11-23 01:21 | +20 | ETH | DOWN | 0.64 | 0.85 | 1.84 |
| 11-23 01:21 | +15 | ETH | DOWN | 0.64 | 0.79 | 1.21 |
| 11-23 01:20 | +10 stop | NEAR | DOWN | 0.62 | 0.47 | -1.85 |
| 11-23 01:20 | +10 stop | ZEC | DOWN | 0.66 | 0.43 | -2.64 |
| 11-23 01:20 | +10 stop | SOL | DOWN | 0.67 | 0.51 | -1.94 |
| 11-23 01:20 | +10 stop | ETH | DOWN | 0.54 | 0.71 | 1.37 |
| 11-23 01:19 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-23 01:19 | +15 | HYPE | DOWN | 0.68 | 0.84 | 1.34 |
| 11-23 01:19 | +10 stop | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 11-23 01:19 | +5 | ZEC | UP | 0.59 | 0.68 | 0.57 |
| 11-23 01:19 | +5 | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-23 01:19 | +10 stop | NEAR | UP | 0.57 | 0.30 | -3.03 |
| 11-23 01:19 | +10 | NEAR | UP | 0.57 | no | -5.88 |
| 11-23 01:19 | +5 | NEAR | UP | 0.57 | no | -5.88 |
| 11-23 01:19 | +5 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 11-23 01:19 | +10 stop | DOGE | DOWN | 0.71 | 0.54 | -2.03 |
