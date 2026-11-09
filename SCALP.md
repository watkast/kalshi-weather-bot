# Range-Scalp Bot

*Updated Mon Nov 09 13:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53735 | 46868 | 6867 (86) | 2 | $-14720.62 | -4.4% |
| **+10¢** | 40135 | 32124 | 8011 (112) | 3 | $-13703.91 | -5.4% |
| **+15¢** | 33633 | 25002 | 8631 (143) | 5 | $-12469.09 | -5.9% |
| **+20¢** | 29928 | 20874 | 9054 (189) | 9 | $-10958.98 | -5.8% |
| **+10¢ (15¢ stop)** | 65465 | 65359 | 106 (63) | 1 | $-24235.11 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 13:36 | +5 | ETH | DOWN | 0.48 | open |  |
| 11-09 13:36 | +5 | ETH | DOWN | 0.51 | 0.59 | 0.45 |
| 11-09 13:35 | +5 | ETH | DOWN | 0.51 | 0.59 | 0.45 |
| 11-09 13:35 | +10 stop | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-09 13:35 | +10 stop | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 11-09 13:35 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 11-09 13:35 | +10 stop | ETH | DOWN | 0.59 | open |  |
| 11-09 13:35 | +5 | ETH | DOWN | 0.59 | 0.68 | 0.57 |
| 11-09 13:34 | +10 stop | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-09 13:34 | +10 stop | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 11-09 13:34 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-09 13:34 | +10 stop | BNB | DOWN | 0.65 | 0.79 | 1.12 |
| 11-09 13:34 | +10 | BNB | DOWN | 0.65 | 0.79 | 1.12 |
| 11-09 13:34 | +5 | BNB | DOWN | 0.65 | 0.73 | 0.50 |
| 11-09 13:34 | +10 stop | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-09 13:34 | +20 | DOGE | DOWN | 0.69 | open |  |
| 11-09 13:34 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-09 13:34 | +10 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-09 13:34 | +5 | DOGE | DOWN | 0.69 | 0.75 | 0.31 |
| 11-09 13:33 | +5 | BTC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-09 13:32 | +10 stop | NEAR | DOWN | 0.68 | 0.37 | -3.43 |
| 11-09 13:32 | +10 stop | ZEC | DOWN | 0.63 | 0.45 | -2.15 |
| 11-09 13:32 | +10 stop | ETH | DOWN | 0.67 | 0.44 | -2.64 |
| 11-09 13:32 | +5 | NEAR | DOWN | 0.64 | 0.71 | 0.42 |
| 11-09 13:32 | +10 stop | BTC | DOWN | 0.64 | 0.45 | -2.25 |
| 11-09 13:32 | +15 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-09 13:32 | +10 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-09 13:32 | +5 | BTC | DOWN | 0.63 | 0.69 | 0.28 |
| 11-09 13:32 | +5 | ETH | DOWN | 0.64 | 0.71 | 0.38 |
| 11-09 13:32 | +10 stop | BNB | DOWN | 0.66 | 0.77 | 0.86 |
| 11-09 13:32 | +10 | BNB | DOWN | 0.66 | 0.77 | 0.86 |
| 11-09 13:32 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.34 |
| 11-09 13:32 | +10 stop | SOL | DOWN | 0.64 | 0.41 | -2.64 |
| 11-09 13:32 | +10 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-09 13:32 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 11-09 13:31 | +10 stop | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 11-09 13:31 | +20 | XRP | DOWN | 0.71 | open |  |
| 11-09 13:31 | +15 | XRP | DOWN | 0.71 | 0.87 | 1.37 |
| 11-09 13:31 | +10 | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 11-09 13:31 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
