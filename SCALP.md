# Range-Scalp Bot

*Updated Wed Nov 25 08:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71653 | 62543 | 9110 (157) | 0 | $-19073.59 | -4.2% |
| **+10¢** | 53443 | 42802 | 10641 (203) | 0 | $-17680.93 | -5.3% |
| **+15¢** | 44758 | 33301 | 11457 (260) | 0 | $-15727.52 | -5.6% |
| **+20¢** | 39852 | 27785 | 12067 (326) | 0 | $-14132.40 | -5.7% |
| **+10¢ (15¢ stop)** | 87248 | 87045 | 203 (123) | 0 | $-32065.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 08:12 | +5 | SOL | DOWN | 0.67 | yes | -6.86 |
| 11-25 08:12 | +10 stop | ETH | DOWN | 0.69 | 0.38 | -3.42 |
| 11-25 08:12 | +5 | ETH | DOWN | 0.69 | yes | -7.04 |
| 11-25 08:12 | +10 stop | SOL | DOWN | 0.70 | 0.52 | -2.13 |
| 11-25 08:12 | +15 | DOGE | UP | 0.63 | 0.82 | 1.62 |
| 11-25 08:12 | +10 | DOGE | UP | 0.64 | 0.82 | 1.52 |
| 11-25 08:12 | +5 | DOGE | UP | 0.64 | 0.82 | 1.52 |
| 11-25 08:12 | +10 stop | DOGE | UP | 0.71 | 0.82 | 0.84 |
| 11-25 08:11 | +10 stop | NEAR | DOWN | 0.55 | 0.38 | -2.05 |
| 11-25 08:11 | +10 stop | SOL | DOWN | 0.71 | 0.55 | -1.93 |
| 11-25 08:11 | +10 | SOL | DOWN | 0.71 | yes | -7.25 |
| 11-25 08:11 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 11-25 08:11 | +10 stop | DOGE | UP | 0.44 | 0.63 | 1.55 |
| 11-25 08:11 | +20 | DOGE | UP | 0.44 | 0.82 | 3.51 |
| 11-25 08:11 | +15 | DOGE | UP | 0.44 | 0.63 | 1.55 |
| 11-25 08:11 | +10 | DOGE | UP | 0.44 | 0.63 | 1.55 |
| 11-25 08:11 | +5 | DOGE | UP | 0.48 | 0.63 | 1.15 |
| 11-25 08:10 | +10 stop | HYPE | DOWN | 0.68 | 0.88 | 1.76 |
| 11-25 08:10 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-25 08:10 | +10 stop | NEAR | UP | 0.60 | 0.35 | -2.83 |
| 11-25 08:08 | +10 stop | BNB | UP | 0.67 | 0.91 | 2.18 |
| 11-25 08:08 | +10 stop | ETH | UP | 0.49 | 0.71 | 1.87 |
| 11-25 08:08 | +10 stop | SOL | UP | 0.64 | 0.48 | -1.96 |
| 11-25 08:07 | +10 stop | ETH | DOWN | 0.44 | 0.59 | 1.15 |
| 11-25 08:07 | +10 stop | HYPE | DOWN | 0.63 | 0.75 | 0.86 |
| 11-25 08:06 | +5 | SOL | UP | 0.69 | 0.81 | 0.94 |
| 11-25 08:06 | +5 | BNB | UP | 0.69 | 0.74 | 0.21 |
| 11-25 08:06 | +5 | ETH | UP | 0.64 | 0.71 | 0.38 |
| 11-25 08:06 | +10 stop | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 11-25 08:06 | +5 | DOGE | UP | 0.68 | 0.90 | 2.00 |
| 11-25 08:04 | +10 stop | NEAR | UP | 0.65 | 0.44 | -2.44 |
| 11-25 08:04 | +10 | NEAR | UP | 0.65 | 0.89 | 2.17 |
| 11-25 08:04 | +5 | NEAR | UP | 0.65 | 0.70 | 0.19 |
| 11-25 08:04 | +5 | ETH | UP | 0.66 | 0.72 | 0.31 |
| 11-25 08:03 | +10 stop | HYPE | UP | 0.56 | 0.39 | -2.04 |
| 11-25 08:03 | +10 stop | SOL | UP | 0.70 | 0.52 | -2.13 |
| 11-25 08:03 | +10 stop | ZEC | DOWN | 0.62 | 0.75 | 0.98 |
| 11-25 08:02 | +10 stop | DOGE | UP | 0.64 | 0.90 | 2.39 |
| 11-25 08:02 | +20 | DOGE | UP | 0.64 | 0.90 | 2.39 |
| 11-25 08:02 | +15 | DOGE | UP | 0.64 | 0.90 | 2.39 |
