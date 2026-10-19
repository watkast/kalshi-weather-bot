# Range-Scalp Bot

*Updated Mon Oct 19 14:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24102 | 20958 | 3144 (31) | 0 | $-7180.35 | -4.7% |
| **+10¢** | 18135 | 14508 | 3627 (46) | 0 | $-6407.14 | -5.6% |
| **+15¢** | 15197 | 11292 | 3905 (69) | 2 | $-5786.41 | -6.1% |
| **+20¢** | 13451 | 9365 | 4086 (87) | 2 | $-5165.96 | -6.1% |
| **+10¢ (15¢ stop)** | 29666 | 29614 | 52 (30) | 0 | $-11252.73 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 14:07 | +10 | DOGE | UP | 0.41 | 0.60 | 1.56 |
| 10-19 14:07 | +5 | DOGE | UP | 0.41 | 0.60 | 1.56 |
| 10-19 14:07 | +10 stop | ETH | DOWN | 0.59 | 0.75 | 1.29 |
| 10-19 14:07 | +20 | ETH | DOWN | 0.59 | 0.82 | 2.02 |
| 10-19 14:07 | +15 | ETH | DOWN | 0.59 | 0.75 | 1.29 |
| 10-19 14:07 | +10 | ETH | DOWN | 0.60 | 0.75 | 1.19 |
| 10-19 14:07 | +5 | ETH | DOWN | 0.56 | 0.66 | 0.66 |
| 10-19 14:07 | +10 stop | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-19 14:07 | +20 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-19 14:07 | +15 | SOL | DOWN | 0.68 | 0.84 | 1.34 |
| 10-19 14:07 | +10 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-19 14:07 | +5 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-19 14:06 | +10 stop | BNB | UP | 0.44 | 0.56 | 0.84 |
| 10-19 14:06 | +20 | BNB | UP | 0.44 | open |  |
| 10-19 14:06 | +15 | BNB | UP | 0.43 | open |  |
| 10-19 14:06 | +10 | BNB | UP | 0.43 | 0.56 | 0.90 |
| 10-19 14:06 | +5 | BNB | UP | 0.43 | 0.56 | 0.90 |
| 10-19 14:06 | +10 stop | DOGE | UP | 0.54 | 0.33 | -2.44 |
| 10-19 14:06 | +20 | DOGE | UP | 0.50 | open |  |
| 10-19 14:06 | +15 | DOGE | UP | 0.50 | open |  |
| 10-19 14:06 | +10 | DOGE | UP | 0.50 | 0.60 | 0.65 |
| 10-19 14:06 | +5 | DOGE | UP | 0.52 | 0.60 | 0.45 |
| 10-19 14:06 | +10 stop | NEAR | DOWN | 0.54 | 0.68 | 1.06 |
| 10-19 14:06 | +20 | NEAR | DOWN | 0.54 | 0.76 | 1.89 |
| 10-19 14:06 | +15 | NEAR | DOWN | 0.53 | 0.68 | 1.16 |
| 10-19 14:06 | +10 | NEAR | DOWN | 0.53 | 0.68 | 1.16 |
| 10-19 14:06 | +5 | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 10-19 14:01 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-19 14:01 | +20 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 10-19 14:01 | +15 | BNB | DOWN | 0.67 | 0.85 | 1.55 |
| 10-19 14:01 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-19 14:01 | +5 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-19 13:52 | +10 stop | NEAR | UP | 0.53 | 0.29 | -2.73 |
| 10-19 13:51 | +10 stop | HYPE | DOWN | 0.58 | 0.72 | 1.07 |
| 10-19 13:50 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-19 13:50 | +10 stop | BNB | UP | 0.50 | 0.30 | -2.33 |
| 10-19 13:50 | +10 stop | SOL | DOWN | 0.56 | 0.80 | 2.10 |
| 10-19 13:50 | +10 | SOL | DOWN | 0.55 | 0.80 | 2.20 |
| 10-19 13:50 | +5 | SOL | DOWN | 0.56 | 0.62 | 0.23 |
| 10-19 13:50 | +10 stop | ETH | DOWN | 0.70 | 0.87 | 1.47 |
