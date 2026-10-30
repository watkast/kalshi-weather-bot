# Range-Scalp Bot

*Updated Fri Oct 30 11:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40674 | 35497 | 5177 (51) | 4 | $-11389.18 | -4.4% |
| **+10¢** | 30309 | 24321 | 5988 (74) | 5 | $-10156.93 | -5.3% |
| **+15¢** | 25344 | 18898 | 6446 (101) | 7 | $-9181.60 | -5.8% |
| **+20¢** | 22493 | 15735 | 6758 (131) | 8 | $-8120.07 | -5.8% |
| **+10¢ (15¢ stop)** | 49598 | 49528 | 70 (37) | 5 | $-18776.49 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 11:33 | +10 stop | SOL | DOWN | 0.57 | open |  |
| 10-30 11:33 | +5 | DOGE | UP | 0.59 | 0.68 | 0.57 |
| 10-30 11:33 | +10 stop | XRP | UP | 0.64 | open |  |
| 10-30 11:33 | +10 | XRP | UP | 0.69 | open |  |
| 10-30 11:33 | +5 | XRP | UP | 0.69 | open |  |
| 10-30 11:32 | +10 stop | NEAR | UP | 0.65 | open |  |
| 10-30 11:32 | +20 | NEAR | UP | 0.65 | open |  |
| 10-30 11:32 | +15 | NEAR | UP | 0.65 | open |  |
| 10-30 11:32 | +10 | NEAR | UP | 0.65 | open |  |
| 10-30 11:32 | +5 | NEAR | UP | 0.65 | open |  |
| 10-30 11:32 | +10 stop | ETH | UP | 0.50 | 0.60 | 0.65 |
| 10-30 11:32 | +20 | ETH | UP | 0.50 | open |  |
| 10-30 11:32 | +15 | ETH | UP | 0.50 | open |  |
| 10-30 11:32 | +10 | ETH | UP | 0.50 | 0.60 | 0.65 |
| 10-30 11:32 | +5 | ETH | UP | 0.50 | 0.58 | 0.44 |
| 10-30 11:32 | +15 | BTC | DOWN | 0.55 | 0.70 | 1.17 |
| 10-30 11:32 | +10 stop | BTC | DOWN | 0.63 | open |  |
| 10-30 11:32 | +10 | BTC | DOWN | 0.65 | open |  |
| 10-30 11:32 | +10 stop | XRP | UP | 0.57 | 0.68 | 0.76 |
| 10-30 11:32 | +20 | XRP | UP | 0.57 | open |  |
| 10-30 11:32 | +15 | XRP | UP | 0.57 | open |  |
| 10-30 11:32 | +10 | XRP | UP | 0.57 | 0.68 | 0.76 |
| 10-30 11:32 | +5 | XRP | UP | 0.57 | 0.68 | 0.76 |
| 10-30 11:32 | +10 stop | SOL | DOWN | 0.64 | 0.48 | -1.95 |
| 10-30 11:32 | +20 | SOL | DOWN | 0.64 | open |  |
| 10-30 11:32 | +15 | SOL | DOWN | 0.63 | open |  |
| 10-30 11:32 | +10 | SOL | DOWN | 0.63 | open |  |
| 10-30 11:32 | +5 | SOL | DOWN | 0.64 | open |  |
| 10-30 11:31 | +10 stop | ZEC | UP | 0.50 | 0.70 | 1.67 |
| 10-30 11:31 | +20 | ZEC | UP | 0.50 | 0.70 | 1.67 |
| 10-30 11:31 | +15 | ZEC | UP | 0.50 | 0.70 | 1.67 |
| 10-30 11:31 | +10 | ZEC | UP | 0.50 | 0.70 | 1.67 |
| 10-30 11:31 | +5 | ZEC | UP | 0.50 | 0.58 | 0.44 |
| 10-30 11:31 | +5 | BTC | DOWN | 0.70 | open |  |
| 10-30 11:31 | +10 stop | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 10-30 11:31 | +20 | DOGE | UP | 0.55 | open |  |
| 10-30 11:31 | +15 | DOGE | UP | 0.55 | open |  |
| 10-30 11:31 | +10 | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 10-30 11:31 | +5 | DOGE | UP | 0.55 | 0.62 | 0.35 |
| 10-30 11:31 | +10 stop | BNB | DOWN | 0.61 | open |  |
