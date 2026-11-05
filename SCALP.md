# Range-Scalp Bot

*Updated Thu Nov 05 15:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48497 | 42258 | 6239 (73) | 2 | $-13793.87 | -4.5% |
| **+10¢** | 36205 | 28958 | 7247 (99) | 5 | $-12624.86 | -5.5% |
| **+15¢** | 30325 | 22519 | 7806 (127) | 6 | $-11539.71 | -6.1% |
| **+20¢** | 26940 | 18762 | 8178 (166) | 8 | $-10193.85 | -6.0% |
| **+10¢ (15¢ stop)** | 59102 | 59009 | 93 (56) | 2 | $-21909.85 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 15:40 | +10 stop | DOGE | UP | 0.62 | open |  |
| 11-05 15:40 | +10 | DOGE | UP | 0.62 | open |  |
| 11-05 15:40 | +5 | DOGE | UP | 0.62 | 0.67 | 0.17 |
| 11-05 15:40 | +10 stop | BNB | UP | 0.68 | open |  |
| 11-05 15:40 | +10 | BNB | UP | 0.69 | open |  |
| 11-05 15:40 | +5 | BNB | UP | 0.68 | open |  |
| 11-05 15:38 | +10 stop | BTC | UP | 0.69 | 0.51 | -2.13 |
| 11-05 15:38 | +10 | BTC | UP | 0.69 | open |  |
| 11-05 15:38 | +5 | BTC | UP | 0.69 | open |  |
| 11-05 15:37 | +10 stop | ZEC | UP | 0.71 | 0.85 | 1.16 |
| 11-05 15:37 | +5 | ZEC | UP | 0.71 | 0.85 | 1.16 |
| 11-05 15:36 | +10 stop | BTC | UP | 0.64 | 0.76 | 0.90 |
| 11-05 15:36 | +10 | BTC | UP | 0.64 | 0.76 | 0.90 |
| 11-05 15:36 | +5 | BTC | UP | 0.65 | 0.76 | 0.81 |
| 11-05 15:36 | +10 stop | DOGE | UP | 0.62 | 0.80 | 1.51 |
| 11-05 15:36 | +10 | DOGE | UP | 0.61 | 0.80 | 1.61 |
| 11-05 15:36 | +5 | DOGE | UP | 0.61 | 0.70 | 0.58 |
| 11-05 15:36 | +10 stop | NEAR | UP | 0.68 | 0.81 | 1.03 |
| 11-05 15:36 | +10 | NEAR | UP | 0.67 | 0.81 | 1.13 |
| 11-05 15:36 | +5 | NEAR | UP | 0.67 | 0.75 | 0.50 |
| 11-05 15:36 | +5 | BNB | UP | 0.68 | 0.80 | 0.92 |
| 11-05 15:35 | +20 | ETH | UP | 0.69 | open |  |
| 11-05 15:35 | +15 | ETH | UP | 0.69 | open |  |
| 11-05 15:35 | +5 | ETH | UP | 0.69 | 0.74 | 0.22 |
| 11-05 15:33 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 11-05 15:33 | +10 | BTC | UP | 0.63 | 0.74 | 0.79 |
| 11-05 15:33 | +5 | BTC | UP | 0.63 | 0.74 | 0.79 |
| 11-05 15:33 | +10 stop | ZEC | UP | 0.68 | 0.80 | 0.92 |
| 11-05 15:33 | +15 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 11-05 15:33 | +10 | ZEC | UP | 0.68 | 0.80 | 0.92 |
| 11-05 15:33 | +5 | ZEC | UP | 0.68 | 0.74 | 0.30 |
| 11-05 15:33 | +10 stop | BNB | UP | 0.67 | 0.80 | 1.02 |
| 11-05 15:33 | +20 | BNB | UP | 0.67 | open |  |
| 11-05 15:33 | +15 | BNB | UP | 0.67 | open |  |
| 11-05 15:33 | +10 | BNB | UP | 0.67 | 0.80 | 1.02 |
| 11-05 15:33 | +5 | BNB | UP | 0.67 | 0.75 | 0.50 |
| 11-05 15:32 | +10 stop | ETH | UP | 0.71 | 0.51 | -2.33 |
| 11-05 15:32 | +10 | ETH | UP | 0.71 | open |  |
| 11-05 15:32 | +10 stop | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 11-05 15:32 | +10 | NEAR | UP | 0.70 | 0.82 | 0.94 |
