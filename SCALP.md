# Range-Scalp Bot

*Updated Tue Oct 27 19:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36941 | 32257 | 4684 (44) | 0 | $-10238.55 | -4.4% |
| **+10¢** | 27595 | 22170 | 5425 (66) | 0 | $-9099.96 | -5.2% |
| **+15¢** | 23089 | 17266 | 5823 (90) | 0 | $-8029.28 | -5.5% |
| **+20¢** | 20466 | 14371 | 6095 (115) | 0 | $-6992.89 | -5.4% |
| **+10¢ (15¢ stop)** | 45255 | 45191 | 64 (33) | 0 | $-17220.18 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 18:57 | +10 stop | DOGE | DOWN | 0.54 | 0.68 | 1.06 |
| 10-27 18:57 | +10 stop | BNB | DOWN | 0.39 | 0.54 | 1.15 |
| 10-27 18:57 | +10 | BNB | DOWN | 0.39 | 0.54 | 1.15 |
| 10-27 18:57 | +5 | BNB | DOWN | 0.39 | 0.54 | 1.15 |
| 10-27 18:55 | +10 stop | HYPE | DOWN | 0.62 | 0.35 | -3.03 |
| 10-27 18:55 | +10 stop | DOGE | DOWN | 0.54 | 0.75 | 1.78 |
| 10-27 18:54 | +10 stop | HYPE | DOWN | 0.69 | 0.54 | -1.87 |
| 10-27 18:52 | +10 stop | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 10-27 18:52 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-27 18:49 | +10 stop | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-27 18:49 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-27 18:49 | +10 stop | XRP | DOWN | 0.68 | 0.86 | 1.55 |
| 10-27 18:49 | +10 stop | DOGE | DOWN | 0.63 | 0.77 | 1.10 |
| 10-27 18:48 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 18:48 | +10 stop | HYPE | UP | 0.60 | 0.44 | -1.95 |
| 10-27 18:48 | +10 | HYPE | UP | 0.60 | 0.89 | 2.66 |
| 10-27 18:48 | +5 | HYPE | UP | 0.60 | 0.89 | 2.66 |
| 10-27 18:48 | +10 stop | SOL | DOWN | 0.59 | 0.71 | 0.88 |
| 10-27 18:48 | +5 | SOL | DOWN | 0.63 | 0.71 | 0.48 |
| 10-27 18:48 | +10 stop | NEAR | UP | 0.69 | 0.83 | 1.15 |
| 10-27 18:48 | +20 | NEAR | UP | 0.69 | 0.99 | 2.81 |
| 10-27 18:48 | +15 | NEAR | UP | 0.69 | 0.85 | 1.36 |
| 10-27 18:48 | +10 | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 10-27 18:48 | +5 | NEAR | UP | 0.68 | 0.77 | 0.61 |
| 10-27 18:48 | +5 | XRP | UP | 0.63 | no | -6.47 |
| 10-27 18:48 | +10 stop | BNB | UP | 0.68 | 0.45 | -2.64 |
| 10-27 18:48 | +20 | BNB | UP | 0.68 | no | -6.96 |
| 10-27 18:48 | +15 | BNB | UP | 0.68 | no | -6.96 |
| 10-27 18:48 | +10 | BNB | UP | 0.68 | 0.80 | 0.92 |
| 10-27 18:48 | +5 | BNB | UP | 0.68 | 0.76 | 0.51 |
| 10-27 18:47 | +5 | SOL | UP | 0.49 | 0.59 | 0.65 |
| 10-27 18:46 | +10 stop | HYPE | UP | 0.50 | 0.64 | 1.05 |
| 10-27 18:46 | +20 | HYPE | UP | 0.50 | 0.89 | 3.65 |
| 10-27 18:46 | +15 | HYPE | UP | 0.50 | 0.89 | 3.65 |
| 10-27 18:46 | +10 | HYPE | UP | 0.50 | 0.64 | 1.05 |
| 10-27 18:46 | +5 | HYPE | UP | 0.50 | 0.57 | 0.34 |
| 10-27 18:46 | +10 stop | SOL | UP | 0.56 | 0.40 | -1.95 |
| 10-27 18:46 | +20 | SOL | UP | 0.56 | no | -5.78 |
| 10-27 18:46 | +15 | SOL | UP | 0.56 | no | -5.78 |
| 10-27 18:46 | +10 | SOL | UP | 0.56 | no | -5.78 |
