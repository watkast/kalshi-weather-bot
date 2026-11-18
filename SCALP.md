# Range-Scalp Bot

*Updated Wed Nov 18 00:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63296 | 55207 | 8089 (118) | 1 | $-17273.10 | -4.3% |
| **+10¢** | 47287 | 37820 | 9467 (159) | 3 | $-16179.07 | -5.4% |
| **+15¢** | 39645 | 29437 | 10208 (203) | 4 | $-14662.79 | -5.9% |
| **+20¢** | 35322 | 24610 | 10712 (258) | 4 | $-12907.52 | -5.8% |
| **+10¢ (15¢ stop)** | 77040 | 76882 | 158 (93) | 3 | $-28382.06 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 00:02 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 11-18 00:02 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-18 00:02 | +15 | ETH | DOWN | 0.68 | open |  |
| 11-18 00:02 | +10 | ETH | DOWN | 0.67 | open |  |
| 11-18 00:02 | +5 | ETH | DOWN | 0.67 | open |  |
| 11-18 00:02 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 11-18 00:02 | +20 | BNB | DOWN | 0.65 | open |  |
| 11-18 00:02 | +15 | BNB | DOWN | 0.64 | open |  |
| 11-18 00:02 | +10 | BNB | DOWN | 0.64 | open |  |
| 11-18 00:02 | +5 | BNB | DOWN | 0.64 | 0.70 | 0.28 |
| 11-18 00:01 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 11-18 00:01 | +20 | SOL | DOWN | 0.64 | open |  |
| 11-18 00:01 | +15 | SOL | DOWN | 0.64 | open |  |
| 11-18 00:01 | +10 | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 11-18 00:01 | +5 | SOL | DOWN | 0.64 | 0.70 | 0.28 |
| 11-18 00:01 | +10 stop | ZEC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-18 00:01 | +20 | ZEC | DOWN | 0.65 | 0.86 | 1.85 |
| 11-18 00:01 | +15 | ZEC | DOWN | 0.66 | 0.86 | 1.77 |
| 11-18 00:01 | +10 | ZEC | DOWN | 0.66 | 0.78 | 0.93 |
| 11-18 00:01 | +5 | ZEC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-18 00:01 | +10 stop | DOGE | DOWN | 0.65 | open |  |
| 11-18 00:01 | +20 | DOGE | DOWN | 0.65 | open |  |
| 11-18 00:01 | +15 | DOGE | DOWN | 0.65 | open |  |
| 11-18 00:01 | +10 | DOGE | DOWN | 0.66 | open |  |
| 11-18 00:01 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 11-17 23:58 | +10 stop | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 11-17 23:58 | +20 | BTC | DOWN | 0.65 | 0.90 | 2.28 |
| 11-17 23:58 | +15 | BTC | DOWN | 0.69 | 0.90 | 1.89 |
| 11-17 23:58 | +10 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 11-17 23:58 | +5 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 11-17 23:53 | +10 stop | XRP | DOWN | 0.65 | 0.78 | 1.01 |
| 11-17 23:53 | +15 | XRP | DOWN | 0.65 | 0.81 | 1.33 |
| 11-17 23:53 | +10 | XRP | DOWN | 0.65 | 0.78 | 1.01 |
| 11-17 23:53 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 11-17 23:53 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-17 23:53 | +10 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-17 23:53 | +5 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-17 23:53 | +10 stop | DOGE | UP | 0.66 | 0.79 | 1.02 |
| 11-17 23:52 | +10 stop | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 11-17 23:52 | +10 stop | NEAR | UP | 0.56 | 0.68 | 0.86 |
