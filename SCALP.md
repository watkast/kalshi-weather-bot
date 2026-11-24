# Range-Scalp Bot

*Updated Tue Nov 24 10:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70854 | 61850 | 9004 (148) | 7 | $-18908.36 | -4.2% |
| **+10¢** | 52845 | 42332 | 10513 (193) | 8 | $-17497.81 | -5.3% |
| **+15¢** | 44267 | 32943 | 11324 (250) | 8 | $-15572.11 | -5.6% |
| **+20¢** | 39415 | 27493 | 11922 (316) | 8 | $-13937.04 | -5.6% |
| **+10¢ (15¢ stop)** | 86258 | 86060 | 198 (118) | 3 | $-31702.30 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 10:31 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-24 10:31 | +10 stop | SOL | DOWN | 0.70 | 0.51 | -2.23 |
| 11-24 10:31 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-24 10:31 | +15 | SOL | DOWN | 0.70 | open |  |
| 11-24 10:31 | +10 | SOL | DOWN | 0.70 | open |  |
| 11-24 10:31 | +5 | SOL | DOWN | 0.70 | open |  |
| 11-24 10:31 | +10 stop | NEAR | DOWN | 0.67 | 0.51 | -1.94 |
| 11-24 10:31 | +20 | NEAR | DOWN | 0.67 | open |  |
| 11-24 10:31 | +15 | NEAR | DOWN | 0.67 | open |  |
| 11-24 10:31 | +10 | NEAR | DOWN | 0.67 | open |  |
| 11-24 10:31 | +5 | NEAR | DOWN | 0.67 | open |  |
| 11-24 10:31 | +10 stop | BNB | DOWN | 0.64 | 0.39 | -2.84 |
| 11-24 10:31 | +20 | BNB | DOWN | 0.64 | open |  |
| 11-24 10:31 | +15 | BNB | DOWN | 0.64 | open |  |
| 11-24 10:31 | +10 | BNB | DOWN | 0.64 | open |  |
| 11-24 10:31 | +5 | BNB | DOWN | 0.64 | open |  |
| 11-24 10:31 | +10 stop | ETH | DOWN | 0.70 | 0.52 | -2.13 |
| 11-24 10:31 | +20 | ETH | DOWN | 0.70 | open |  |
| 11-24 10:31 | +15 | ETH | DOWN | 0.70 | open |  |
| 11-24 10:31 | +10 | ETH | DOWN | 0.70 | open |  |
| 11-24 10:31 | +5 | ETH | DOWN | 0.70 | open |  |
| 11-24 10:31 | +10 stop | DOGE | DOWN | 0.64 | 0.46 | -2.14 |
| 11-24 10:31 | +20 | DOGE | DOWN | 0.63 | open |  |
| 11-24 10:31 | +15 | DOGE | DOWN | 0.63 | open |  |
| 11-24 10:31 | +10 | DOGE | DOWN | 0.63 | open |  |
| 11-24 10:31 | +5 | DOGE | DOWN | 0.60 | open |  |
| 11-24 10:30 | +10 stop | HYPE | DOWN | 0.58 | open |  |
| 11-24 10:30 | +20 | HYPE | DOWN | 0.58 | open |  |
| 11-24 10:30 | +15 | HYPE | DOWN | 0.58 | open |  |
| 11-24 10:30 | +10 | HYPE | DOWN | 0.58 | open |  |
| 11-24 10:30 | +5 | HYPE | DOWN | 0.58 | open |  |
| 11-24 10:30 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 11-24 10:30 | +20 | XRP | DOWN | 0.68 | open |  |
| 11-24 10:30 | +15 | XRP | DOWN | 0.68 | open |  |
| 11-24 10:30 | +10 | XRP | DOWN | 0.68 | open |  |
| 11-24 10:30 | +5 | XRP | DOWN | 0.68 | open |  |
| 11-24 10:30 | +10 stop | ZEC | DOWN | 0.60 | open |  |
| 11-24 10:30 | +20 | ZEC | DOWN | 0.60 | open |  |
| 11-24 10:30 | +15 | ZEC | DOWN | 0.60 | open |  |
| 11-24 10:30 | +10 | ZEC | DOWN | 0.60 | open |  |
