# Range-Scalp Bot

*Updated Fri Oct 09 05:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8577 | 7421 | 1156 (13) | 5 | $-2796.24 | -5.2% |
| **+10¢** | 6493 | 5131 | 1362 (25) | 6 | $-2720.62 | -6.7% |
| **+15¢** | 5479 | 4046 | 1433 (37) | 6 | $-2192.09 | -6.4% |
| **+20¢** | 4875 | 3387 | 1488 (45) | 6 | $-1808.44 | -5.9% |
| **+10¢ (15¢ stop)** | 10442 | 10412 | 30 (19) | 0 | $-3882.03 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 05:08 | +10 stop | ZEC | DOWN | 0.68 | 0.32 | -3.92 |
| 10-09 05:07 | +10 stop | ETH | UP | 0.68 | 0.84 | 1.34 |
| 10-09 05:07 | +10 stop | BTC | UP | 0.71 | 0.83 | 0.95 |
| 10-09 05:07 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 10-09 05:05 | +10 stop | ZEC | UP | 0.67 | 0.46 | -2.44 |
| 10-09 05:04 | +10 stop | ZEC | UP | 0.69 | 0.53 | -1.93 |
| 10-09 05:02 | +10 stop | HYPE | UP | 0.66 | 0.83 | 1.40 |
| 10-09 05:02 | +10 stop | BNB | UP | 0.66 | 0.80 | 1.08 |
| 10-09 05:02 | +20 | BNB | UP | 0.66 | 0.95 | 2.70 |
| 10-09 05:02 | +15 | BNB | UP | 0.66 | 0.83 | 1.40 |
| 10-09 05:02 | +10 | BNB | UP | 0.66 | 0.80 | 1.08 |
| 10-09 05:02 | +5 | BNB | UP | 0.66 | 0.73 | 0.40 |
| 10-09 05:02 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-09 05:02 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 10-09 05:02 | +5 | BTC | DOWN | 0.41 | 0.57 | 1.25 |
| 10-09 05:01 | +10 stop | ETH | DOWN | 0.68 | 0.34 | -3.72 |
| 10-09 05:01 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-09 05:01 | +15 | ETH | DOWN | 0.68 | open |  |
| 10-09 05:01 | +10 | ETH | DOWN | 0.68 | open |  |
| 10-09 05:01 | +5 | ETH | DOWN | 0.68 | open |  |
| 10-09 05:01 | +10 stop | ZEC | DOWN | 0.67 | 0.47 | -2.34 |
| 10-09 05:01 | +20 | ZEC | DOWN | 0.67 | open |  |
| 10-09 05:01 | +15 | ZEC | DOWN | 0.67 | open |  |
| 10-09 05:01 | +10 | ZEC | DOWN | 0.67 | open |  |
| 10-09 05:01 | +5 | ZEC | DOWN | 0.67 | open |  |
| 10-09 05:01 | +10 stop | XRP | DOWN | 0.63 | 0.34 | -3.23 |
| 10-09 05:01 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-09 05:01 | +15 | XRP | DOWN | 0.63 | open |  |
| 10-09 05:01 | +10 | XRP | DOWN | 0.63 | open |  |
| 10-09 05:01 | +5 | XRP | DOWN | 0.63 | open |  |
| 10-09 05:01 | +10 stop | SOL | DOWN | 0.57 | 0.28 | -3.23 |
| 10-09 05:01 | +20 | SOL | DOWN | 0.57 | open |  |
| 10-09 05:01 | +15 | SOL | DOWN | 0.57 | open |  |
| 10-09 05:01 | +10 | SOL | DOWN | 0.57 | open |  |
| 10-09 05:01 | +5 | SOL | DOWN | 0.58 | open |  |
| 10-09 05:01 | +10 stop | BTC | DOWN | 0.58 | 0.37 | -2.45 |
| 10-09 05:01 | +20 | BTC | DOWN | 0.58 | open |  |
| 10-09 05:01 | +15 | BTC | DOWN | 0.58 | open |  |
| 10-09 05:01 | +10 | BTC | DOWN | 0.58 | open |  |
| 10-09 05:01 | +5 | BTC | DOWN | 0.58 | 0.63 | 0.15 |
