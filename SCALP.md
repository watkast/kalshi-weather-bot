# Range-Scalp Bot

*Updated Thu Nov 05 13:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48316 | 42096 | 6220 (73) | 5 | $-13769.88 | -4.5% |
| **+10¢** | 36075 | 28849 | 7226 (99) | 6 | $-12621.98 | -5.6% |
| **+15¢** | 30230 | 22449 | 7781 (127) | 6 | $-11515.03 | -6.1% |
| **+20¢** | 26855 | 18704 | 8151 (166) | 6 | $-10160.02 | -6.0% |
| **+10¢ (15¢ stop)** | 58893 | 58800 | 93 (56) | 0 | $-21857.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 13:28 | +10 stop | BTC | UP | 0.58 | 0.71 | 0.97 |
| 11-05 13:28 | +10 stop | ETH | UP | 0.50 | 0.69 | 1.57 |
| 11-05 13:27 | +10 stop | SOL | DOWN | 0.44 | 0.57 | 0.94 |
| 11-05 13:27 | +5 | SOL | DOWN | 0.44 | 0.57 | 0.94 |
| 11-05 13:27 | +10 stop | SOL | UP | 0.40 | 0.59 | 1.56 |
| 11-05 13:27 | +5 | SOL | UP | 0.40 | 0.59 | 1.56 |
| 11-05 13:27 | +10 stop | ETH | UP | 0.44 | 0.54 | 0.64 |
| 11-05 13:26 | +10 stop | NEAR | UP | 0.52 | 0.17 | -3.78 |
| 11-05 13:26 | +10 stop | DOGE | DOWN | 0.62 | 0.82 | 1.72 |
| 11-05 13:26 | +10 stop | BTC | UP | 0.65 | 0.49 | -1.94 |
| 11-05 13:26 | +10 stop | BNB | UP | 0.68 | 0.83 | 1.24 |
| 11-05 13:26 | +10 stop | XRP | DOWN | 0.60 | 0.81 | 1.82 |
| 11-05 13:25 | +10 stop | BNB | DOWN | 0.39 | 0.61 | 1.86 |
| 11-05 13:25 | +10 stop | NEAR | DOWN | 0.68 | 0.52 | -1.96 |
| 11-05 13:24 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.71 |
| 11-05 13:24 | +10 stop | ETH | DOWN | 0.54 | 0.68 | 1.06 |
| 11-05 13:24 | +10 stop | BNB | UP | 0.60 | 0.44 | -1.95 |
| 11-05 13:24 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 11-05 13:24 | +10 stop | SOL | UP | 0.54 | 0.67 | 0.96 |
| 11-05 13:24 | +5 | SOL | UP | 0.54 | 0.59 | 0.15 |
| 11-05 13:23 | +10 stop | NEAR | UP | 0.62 | 0.43 | -2.25 |
| 11-05 13:23 | +10 stop | XRP | DOWN | 0.52 | 0.66 | 1.06 |
| 11-05 13:22 | +10 stop | BNB | UP | 0.56 | 0.71 | 1.17 |
| 11-05 13:22 | +10 stop | DOGE | UP | 0.53 | 0.31 | -2.53 |
| 11-05 13:21 | +10 stop | ETH | DOWN | 0.57 | 0.41 | -1.95 |
| 11-05 13:21 | +10 stop | NEAR | DOWN | 0.62 | 0.45 | -2.05 |
| 11-05 13:21 | +10 stop | BTC | UP | 0.53 | 0.70 | 1.37 |
| 11-05 13:21 | +10 stop | SOL | UP | 0.54 | 0.70 | 1.27 |
| 11-05 13:20 | +10 stop | BTC | DOWN | 0.54 | 0.35 | -2.24 |
| 11-05 13:20 | +10 stop | SOL | DOWN | 0.57 | 0.36 | -2.45 |
| 11-05 13:20 | +10 stop | ETH | DOWN | 0.68 | 0.45 | -2.64 |
| 11-05 13:20 | +10 stop | NEAR | DOWN | 0.68 | 0.49 | -2.24 |
| 11-05 13:19 | +10 stop | SOL | UP | 0.44 | 0.55 | 0.74 |
| 11-05 13:19 | +10 stop | DOGE | DOWN | 0.56 | 0.41 | -1.85 |
| 11-05 13:19 | +10 stop | BNB | DOWN | 0.59 | 0.42 | -2.10 |
| 11-05 13:19 | +10 stop | XRP | DOWN | 0.64 | 0.49 | -1.87 |
| 11-05 13:18 | +5 | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-05 13:18 | +5 | DOGE | UP | 0.54 | open |  |
| 11-05 13:18 | +15 | SOL | UP | 0.59 | open |  |
| 11-05 13:18 | +5 | SOL | UP | 0.59 | 0.70 | 0.78 |
