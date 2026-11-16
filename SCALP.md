# Range-Scalp Bot

*Updated Mon Nov 16 12:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62048 | 54140 | 7908 (115) | 0 | $-16737.95 | -4.3% |
| **+10¢** | 46338 | 37083 | 9255 (157) | 0 | $-15610.96 | -5.4% |
| **+15¢** | 38829 | 28847 | 9982 (196) | 0 | $-14211.57 | -5.8% |
| **+20¢** | 34614 | 24148 | 10466 (249) | 2 | $-12388.17 | -5.7% |
| **+10¢ (15¢ stop)** | 75509 | 75355 | 154 (90) | 0 | $-27835.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 12:02 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 11-16 12:01 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-16 12:01 | +20 | DOGE | DOWN | 0.70 | 0.91 | 1.85 |
| 11-16 12:01 | +15 | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
| 11-16 12:01 | +10 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-16 12:01 | +10 stop | NEAR | DOWN | 0.67 | 0.79 | 0.94 |
| 11-16 12:01 | +20 | NEAR | DOWN | 0.67 | open |  |
| 11-16 12:01 | +15 | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
| 11-16 12:01 | +10 | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 11-16 12:01 | +5 | NEAR | DOWN | 0.67 | 0.76 | 0.61 |
| 11-16 12:01 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-16 12:01 | +20 | ETH | DOWN | 0.70 | open |  |
| 11-16 12:01 | +15 | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 11-16 12:01 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 12:01 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 11-16 12:01 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-16 12:01 | +20 | BTC | DOWN | 0.63 | 0.84 | 1.83 |
| 11-16 12:01 | +15 | BTC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-16 12:01 | +10 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-16 12:01 | +5 | BTC | DOWN | 0.63 | 0.70 | 0.38 |
| 11-16 12:01 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-16 12:01 | +20 | SOL | DOWN | 0.68 | 0.91 | 2.05 |
| 11-16 12:01 | +15 | SOL | DOWN | 0.69 | 0.84 | 1.25 |
| 11-16 12:01 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-16 12:01 | +5 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-16 12:01 | +10 stop | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 11-16 12:01 | +20 | BNB | DOWN | 0.59 | 0.81 | 1.92 |
| 11-16 12:01 | +15 | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 11-16 12:01 | +10 | BNB | DOWN | 0.60 | 0.71 | 0.78 |
| 11-16 12:01 | +5 | BNB | DOWN | 0.60 | 0.69 | 0.58 |
| 11-16 11:58 | +10 stop | ETH | DOWN | 0.54 | 0.77 | 1.99 |
| 11-16 11:57 | +10 stop | NEAR | UP | 0.29 | 0.57 | 2.47 |
| 11-16 11:57 | +10 | NEAR | UP | 0.32 | 0.57 | 2.16 |
| 11-16 11:57 | +5 | NEAR | UP | 0.29 | 0.57 | 2.47 |
| 11-16 11:57 | +10 stop | DOGE | UP | 0.32 | 0.53 | 1.76 |
| 11-16 11:57 | +10 stop | SOL | UP | 0.34 | 0.54 | 1.66 |
| 11-16 11:56 | +10 stop | NEAR | UP | 0.67 | 0.80 | 1.02 |
| 11-16 11:56 | +20 | NEAR | UP | 0.67 | no | -6.86 |
| 11-16 11:56 | +15 | NEAR | UP | 0.67 | no | -6.86 |
| 11-16 11:56 | +10 | NEAR | UP | 0.67 | 0.80 | 1.02 |
