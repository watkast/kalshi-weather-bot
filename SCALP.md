# Range-Scalp Bot

*Updated Thu Nov 19 07:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64969 | 56702 | 8267 (124) | 1 | $-17481.91 | -4.3% |
| **+10¢** | 48531 | 38859 | 9672 (165) | 1 | $-16272.38 | -5.3% |
| **+15¢** | 40695 | 30264 | 10431 (210) | 1 | $-14682.08 | -5.7% |
| **+20¢** | 36241 | 25286 | 10955 (265) | 1 | $-12985.08 | -5.7% |
| **+10¢ (15¢ stop)** | 79064 | 78900 | 164 (98) | 1 | $-29039.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 07:30 | +10 stop | NEAR | UP | 0.58 | open |  |
| 11-19 07:30 | +20 | NEAR | UP | 0.58 | open |  |
| 11-19 07:30 | +15 | NEAR | UP | 0.58 | open |  |
| 11-19 07:30 | +10 | NEAR | UP | 0.58 | open |  |
| 11-19 07:30 | +5 | NEAR | UP | 0.58 | open |  |
| 11-19 07:28 | +10 stop | HYPE | DOWN | 0.63 | 0.80 | 1.43 |
| 11-19 07:28 | +20 | HYPE | DOWN | 0.63 | 0.97 | 3.25 |
| 11-19 07:28 | +15 | HYPE | DOWN | 0.63 | 0.80 | 1.43 |
| 11-19 07:28 | +10 | HYPE | DOWN | 0.63 | 0.80 | 1.42 |
| 11-19 07:28 | +5 | HYPE | DOWN | 0.63 | 0.80 | 1.41 |
| 11-19 07:27 | +10 stop | ZEC | UP | 0.60 | 0.24 | -3.90 |
| 11-19 07:26 | +10 stop | ETH | UP | 0.61 | 0.74 | 0.99 |
| 11-19 07:25 | +10 stop | HYPE | DOWN | 0.64 | 0.79 | 1.21 |
| 11-19 07:25 | +10 stop | ZEC | UP | 0.52 | 0.65 | 0.96 |
| 11-19 07:24 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-19 07:24 | +5 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-19 07:24 | +10 stop | ETH | UP | 0.71 | 0.56 | -1.83 |
| 11-19 07:24 | +20 | ETH | UP | 0.71 | 0.95 | 2.23 |
| 11-19 07:24 | +15 | ETH | UP | 0.71 | 0.87 | 1.37 |
| 11-19 07:24 | +10 | ETH | UP | 0.71 | 0.82 | 0.84 |
| 11-19 07:24 | +5 | ETH | UP | 0.71 | 0.77 | 0.32 |
| 11-19 07:24 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-19 07:23 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-19 07:23 | +10 stop | ZEC | UP | 0.51 | 0.61 | 0.65 |
| 11-19 07:23 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.85 |
| 11-19 07:23 | +10 stop | BNB | DOWN | 0.58 | 0.69 | 0.76 |
| 11-19 07:23 | +10 stop | HYPE | DOWN | 0.57 | 0.70 | 0.97 |
| 11-19 07:23 | +20 | HYPE | DOWN | 0.57 | 0.79 | 1.90 |
| 11-19 07:23 | +15 | HYPE | DOWN | 0.57 | 0.79 | 1.90 |
| 11-19 07:23 | +10 | HYPE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-19 07:23 | +5 | HYPE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-19 07:23 | +10 | ZEC | UP | 0.69 | no | -7.05 |
| 11-19 07:23 | +5 | ZEC | UP | 0.69 | no | -7.05 |
| 11-19 07:22 | +10 stop | DOGE | UP | 0.54 | 0.37 | -2.05 |
| 11-19 07:22 | +10 | DOGE | UP | 0.54 | no | -5.58 |
| 11-19 07:22 | +5 | DOGE | UP | 0.54 | no | -5.58 |
| 11-19 07:22 | +10 stop | BNB | UP | 0.52 | 0.32 | -2.34 |
| 11-19 07:22 | +10 stop | ZEC | UP | 0.66 | 0.51 | -1.84 |
| 11-19 07:22 | +10 stop | NEAR | UP | 0.62 | 0.44 | -2.15 |
| 11-19 07:22 | +10 stop | SOL | DOWN | 0.58 | 0.69 | 0.77 |
