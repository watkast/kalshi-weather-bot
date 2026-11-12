# Range-Scalp Bot

*Updated Thu Nov 12 02:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56427 | 49196 | 7231 (98) | 9 | $-15483.70 | -4.4% |
| **+10¢** | 42171 | 33736 | 8435 (128) | 9 | $-14430.68 | -5.4% |
| **+15¢** | 35366 | 26277 | 9089 (162) | 8 | $-13115.10 | -5.9% |
| **+20¢** | 31505 | 21970 | 9535 (212) | 9 | $-11471.34 | -5.8% |
| **+10¢ (15¢ stop)** | 68798 | 68675 | 123 (73) | 0 | $-25395.02 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 02:09 | +10 stop | XRP | UP | 0.59 | 0.72 | 0.98 |
| 11-12 02:09 | +10 stop | BNB | UP | 0.67 | 0.77 | 0.71 |
| 11-12 02:08 | +10 stop | DOGE | UP | 0.61 | 0.46 | -1.85 |
| 11-12 02:08 | +10 stop | DOGE | UP | 0.69 | 0.54 | -1.83 |
| 11-12 02:07 | +10 stop | XRP | UP | 0.68 | 0.51 | -2.04 |
| 11-12 02:06 | +10 stop | DOGE | UP | 0.54 | 0.73 | 1.58 |
| 11-12 02:06 | +10 stop | BTC | UP | 0.61 | 0.71 | 0.68 |
| 11-12 02:05 | +10 stop | ETH | UP | 0.68 | 0.87 | 1.66 |
| 11-12 02:04 | +10 stop | BNB | DOWN | 0.54 | 0.39 | -1.85 |
| 11-12 02:04 | +10 stop | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 11-12 02:04 | +10 stop | SOL | UP | 0.58 | 0.76 | 1.49 |
| 11-12 02:04 | +15 | SOL | UP | 0.56 | 0.76 | 1.70 |
| 11-12 02:04 | +10 stop | NEAR | DOWN | 0.68 | 0.50 | -2.14 |
| 11-12 02:04 | +10 | NEAR | DOWN | 0.68 | open |  |
| 11-12 02:04 | +5 | NEAR | DOWN | 0.68 | open |  |
| 11-12 02:03 | +10 stop | ZEC | UP | 0.53 | 0.67 | 1.06 |
| 11-12 02:03 | +10 stop | SOL | DOWN | 0.62 | 0.46 | -1.95 |
| 11-12 02:03 | +10 stop | HYPE | UP | 0.53 | 0.71 | 1.47 |
| 11-12 02:02 | +10 stop | DOGE | DOWN | 0.71 | 0.52 | -2.23 |
| 11-12 02:02 | +20 | DOGE | DOWN | 0.71 | open |  |
| 11-12 02:02 | +15 | DOGE | DOWN | 0.71 | open |  |
| 11-12 02:02 | +10 | DOGE | DOWN | 0.71 | open |  |
| 11-12 02:02 | +5 | DOGE | DOWN | 0.71 | open |  |
| 11-12 02:02 | +10 stop | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 02:02 | +20 | NEAR | DOWN | 0.62 | open |  |
| 11-12 02:02 | +15 | NEAR | DOWN | 0.62 | open |  |
| 11-12 02:02 | +10 | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 02:02 | +5 | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 02:02 | +10 stop | XRP | DOWN | 0.62 | 0.30 | -3.52 |
| 11-12 02:02 | +20 | XRP | DOWN | 0.62 | open |  |
| 11-12 02:02 | +15 | XRP | DOWN | 0.62 | open |  |
| 11-12 02:02 | +10 | XRP | DOWN | 0.62 | open |  |
| 11-12 02:02 | +5 | XRP | DOWN | 0.62 | open |  |
| 11-12 02:02 | +10 stop | BNB | DOWN | 0.69 | 0.52 | -2.02 |
| 11-12 02:02 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-12 02:02 | +15 | BNB | DOWN | 0.69 | open |  |
| 11-12 02:02 | +10 | BNB | DOWN | 0.69 | open |  |
| 11-12 02:02 | +5 | BNB | DOWN | 0.69 | open |  |
| 11-12 02:02 | +10 stop | BTC | DOWN | 0.65 | 0.50 | -1.84 |
| 11-12 02:02 | +20 | BTC | DOWN | 0.66 | open |  |
