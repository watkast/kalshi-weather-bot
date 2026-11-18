# Range-Scalp Bot

*Updated Wed Nov 18 08:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63828 | 55669 | 8159 (119) | 1 | $-17440.49 | -4.3% |
| **+10¢** | 47694 | 38144 | 9550 (160) | 1 | $-16354.17 | -5.5% |
| **+15¢** | 39989 | 29692 | 10297 (205) | 1 | $-14822.10 | -5.9% |
| **+20¢** | 35616 | 24807 | 10809 (260) | 1 | $-13109.44 | -5.9% |
| **+10¢ (15¢ stop)** | 77651 | 77493 | 158 (93) | 1 | $-28506.80 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 08:09 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 11-18 08:09 | +5 | XRP | DOWN | 0.68 | open |  |
| 11-18 08:07 | +10 stop | DOGE | DOWN | 0.58 | 0.72 | 1.07 |
| 11-18 08:07 | +10 stop | XRP | UP | 0.60 | 0.70 | 0.68 |
| 11-18 08:06 | +5 | XRP | UP | 0.63 | 0.70 | 0.38 |
| 11-18 08:05 | +10 stop | XRP | DOWN | 0.52 | 0.33 | -2.24 |
| 11-18 08:05 | +5 | XRP | DOWN | 0.52 | 0.59 | 0.35 |
| 11-18 08:04 | +10 stop | DOGE | DOWN | 0.63 | 0.48 | -1.85 |
| 11-18 08:02 | +5 | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-18 08:02 | +10 stop | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 11-18 08:02 | +20 | XRP | DOWN | 0.60 | open |  |
| 11-18 08:02 | +15 | XRP | DOWN | 0.62 | open |  |
| 11-18 08:02 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-18 08:02 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 11-18 08:01 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-18 08:01 | +20 | SOL | DOWN | 0.71 | 0.91 | 1.80 |
| 11-18 08:01 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 11-18 08:01 | +10 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-18 08:01 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 11-18 08:01 | +10 stop | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-18 08:01 | +20 | HYPE | DOWN | 0.67 | 0.87 | 1.76 |
| 11-18 08:01 | +15 | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-18 08:01 | +10 | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-18 08:01 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.30 |
| 11-18 08:01 | +10 stop | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 11-18 08:01 | +20 | NEAR | DOWN | 0.61 | 0.85 | 2.14 |
| 11-18 08:01 | +15 | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 11-18 08:01 | +10 | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 11-18 08:01 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 11-18 08:00 | +10 stop | DOGE | DOWN | 0.70 | 0.54 | -1.93 |
| 11-18 08:00 | +20 | DOGE | DOWN | 0.70 | 0.92 | 1.94 |
| 11-18 08:00 | +15 | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
| 11-18 08:00 | +10 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-18 08:00 | +5 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-18 07:46 | +10 stop | ETH | UP | 0.62 | 0.82 | 1.72 |
| 11-18 07:46 | +20 | ETH | UP | 0.62 | 0.82 | 1.72 |
| 11-18 07:46 | +15 | ETH | UP | 0.62 | 0.82 | 1.72 |
| 11-18 07:46 | +10 | ETH | UP | 0.62 | 0.82 | 1.72 |
| 11-18 07:46 | +5 | ETH | UP | 0.62 | 0.82 | 1.72 |
| 11-18 07:46 | +10 stop | BNB | UP | 0.64 | 0.87 | 2.05 |
