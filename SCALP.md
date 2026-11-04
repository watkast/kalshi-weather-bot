# Range-Scalp Bot

*Updated Wed Nov 04 11:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47220 | 41125 | 6095 (72) | 4 | $-13559.39 | -4.6% |
| **+10¢** | 35266 | 28196 | 7070 (97) | 7 | $-12387.84 | -5.6% |
| **+15¢** | 29530 | 21917 | 7613 (125) | 7 | $-11358.29 | -6.1% |
| **+20¢** | 26233 | 18259 | 7974 (165) | 7 | $-10019.04 | -6.1% |
| **+10¢ (15¢ stop)** | 57555 | 57462 | 93 (56) | 0 | $-21469.27 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 11:53 | +10 stop | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 11-04 11:52 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-04 11:52 | +5 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 11-04 11:52 | +10 stop | BNB | UP | 0.58 | 0.30 | -3.17 |
| 11-04 11:52 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 11-04 11:52 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-04 11:52 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-04 11:51 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-04 11:50 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-04 11:50 | +5 | ETH | DOWN | 0.58 | 0.67 | 0.56 |
| 11-04 11:50 | +10 stop | DOGE | UP | 0.51 | 0.35 | -1.94 |
| 11-04 11:50 | +10 stop | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-04 11:50 | +5 | HYPE | DOWN | 0.62 | 0.69 | 0.38 |
| 11-04 11:50 | +5 | DOGE | UP | 0.53 | open |  |
| 11-04 11:49 | +10 stop | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-04 11:49 | +10 stop | BNB | DOWN | 0.63 | 0.39 | -2.74 |
| 11-04 11:49 | +10 stop | SOL | DOWN | 0.60 | 0.72 | 0.88 |
| 11-04 11:49 | +5 | SOL | DOWN | 0.64 | 0.72 | 0.48 |
| 11-04 11:49 | +10 stop | DOGE | DOWN | 0.59 | 0.40 | -2.24 |
| 11-04 11:49 | +5 | DOGE | DOWN | 0.57 | 0.64 | 0.35 |
| 11-04 11:48 | +10 stop | BTC | DOWN | 0.70 | 0.54 | -1.93 |
| 11-04 11:48 | +5 | SOL | UP | 0.31 | 0.55 | 2.07 |
| 11-04 11:48 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-04 11:48 | +10 stop | ZEC | DOWN | 0.55 | 0.75 | 1.68 |
| 11-04 11:47 | +10 stop | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 11-04 11:47 | +20 | NEAR | DOWN | 0.65 | 0.85 | 1.75 |
| 11-04 11:47 | +15 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-04 11:47 | +10 | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 11-04 11:47 | +5 | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 11-04 11:47 | +10 stop | ETH | UP | 0.42 | 0.22 | -2.31 |
| 11-04 11:47 | +20 | ETH | UP | 0.42 | open |  |
| 11-04 11:47 | +15 | ETH | UP | 0.42 | open |  |
| 11-04 11:47 | +10 | ETH | UP | 0.43 | open |  |
| 11-04 11:47 | +5 | ETH | UP | 0.43 | 0.49 | 0.24 |
| 11-04 11:47 | +5 | HYPE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-04 11:47 | +10 stop | DOGE | UP | 0.52 | 0.33 | -2.24 |
| 11-04 11:47 | +20 | DOGE | UP | 0.54 | open |  |
| 11-04 11:47 | +15 | DOGE | UP | 0.54 | open |  |
| 11-04 11:47 | +10 | DOGE | UP | 0.54 | open |  |
| 11-04 11:47 | +5 | DOGE | UP | 0.54 | 0.60 | 0.25 |
