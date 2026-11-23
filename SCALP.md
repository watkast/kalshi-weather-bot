# Range-Scalp Bot

*Updated Mon Nov 23 00:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69251 | 60420 | 8831 (146) | 6 | $-18676.41 | -4.3% |
| **+10¢** | 51683 | 41373 | 10310 (189) | 5 | $-17322.36 | -5.3% |
| **+15¢** | 43315 | 32201 | 11114 (244) | 7 | $-15525.06 | -5.7% |
| **+20¢** | 38576 | 26893 | 11683 (305) | 7 | $-13818.18 | -5.7% |
| **+10¢ (15¢ stop)** | 84335 | 84145 | 190 (118) | 5 | $-31031.67 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 00:04 | +5 | BNB | UP | 0.68 | open |  |
| 11-23 00:04 | +5 | ETH | UP | 0.57 | open |  |
| 11-23 00:03 | +5 | BTC | DOWN | 0.55 | open |  |
| 11-23 00:03 | +10 stop | BTC | DOWN | 0.60 | open |  |
| 11-23 00:03 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 11-23 00:03 | +5 | ETH | UP | 0.59 | 0.64 | 0.16 |
| 11-23 00:02 | +10 stop | SOL | DOWN | 0.62 | open |  |
| 11-23 00:02 | +20 | SOL | DOWN | 0.62 | open |  |
| 11-23 00:02 | +15 | SOL | DOWN | 0.62 | open |  |
| 11-23 00:02 | +10 | SOL | DOWN | 0.62 | open |  |
| 11-23 00:02 | +5 | SOL | DOWN | 0.62 | open |  |
| 11-23 00:02 | +10 stop | ETH | UP | 0.56 | open |  |
| 11-23 00:02 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-23 00:02 | +20 | BTC | DOWN | 0.56 | open |  |
| 11-23 00:02 | +15 | BTC | DOWN | 0.56 | open |  |
| 11-23 00:02 | +10 | BTC | DOWN | 0.57 | open |  |
| 11-23 00:02 | +5 | BTC | DOWN | 0.57 | 0.63 | 0.25 |
| 11-23 00:01 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 11-23 00:01 | +20 | ZEC | DOWN | 0.65 | open |  |
| 11-23 00:01 | +15 | ZEC | DOWN | 0.64 | open |  |
| 11-23 00:01 | +10 | ZEC | DOWN | 0.64 | open |  |
| 11-23 00:01 | +5 | ZEC | DOWN | 0.64 | open |  |
| 11-23 00:01 | +10 stop | BNB | UP | 0.59 | 0.72 | 0.96 |
| 11-23 00:01 | +20 | BNB | UP | 0.60 | open |  |
| 11-23 00:01 | +15 | BNB | UP | 0.60 | open |  |
| 11-23 00:01 | +10 | BNB | UP | 0.59 | 0.72 | 0.95 |
| 11-23 00:01 | +5 | BNB | UP | 0.59 | 0.66 | 0.37 |
| 11-23 00:00 | +10 stop | DOGE | UP | 0.55 | open |  |
| 11-23 00:00 | +20 | DOGE | UP | 0.56 | open |  |
| 11-23 00:00 | +15 | DOGE | UP | 0.56 | open |  |
| 11-23 00:00 | +10 | DOGE | UP | 0.56 | open |  |
| 11-23 00:00 | +5 | DOGE | UP | 0.58 | open |  |
| 11-23 00:00 | +10 stop | ETH | UP | 0.61 | 0.00 | -6.27 |
| 11-23 00:00 | +20 | ETH | UP | 0.62 | open |  |
| 11-23 00:00 | +15 | ETH | UP | 0.62 | open |  |
| 11-23 00:00 | +10 | ETH | UP | 0.63 | open |  |
| 11-23 00:00 | +5 | ETH | UP | 0.63 | 0.68 | 0.17 |
| 11-22 23:58 | +10 stop | BNB | DOWN | 0.54 | 0.24 | -3.31 |
| 11-22 23:58 | +20 | BNB | DOWN | 0.61 | yes | -6.27 |
| 11-22 23:58 | +15 | BNB | DOWN | 0.61 | yes | -6.27 |
