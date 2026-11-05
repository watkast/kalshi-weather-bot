# Range-Scalp Bot

*Updated Thu Nov 05 17:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48605 | 42360 | 6245 (73) | 3 | $-13774.95 | -4.5% |
| **+10¢** | 36275 | 29017 | 7258 (99) | 4 | $-12630.32 | -5.5% |
| **+15¢** | 30385 | 22566 | 7819 (127) | 6 | $-11543.36 | -6.1% |
| **+20¢** | 26996 | 18803 | 8193 (166) | 6 | $-10196.70 | -6.0% |
| **+10¢ (15¢ stop)** | 59228 | 59135 | 93 (56) | 4 | $-21957.30 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 17:01 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 11-05 17:01 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-05 17:01 | +15 | NEAR | DOWN | 0.70 | open |  |
| 11-05 17:01 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-05 17:01 | +5 | NEAR | DOWN | 0.71 | open |  |
| 11-05 17:01 | +10 stop | BNB | DOWN | 0.71 | open |  |
| 11-05 17:01 | +20 | BNB | DOWN | 0.71 | open |  |
| 11-05 17:01 | +15 | BNB | DOWN | 0.71 | open |  |
| 11-05 17:01 | +10 | BNB | DOWN | 0.71 | open |  |
| 11-05 17:01 | +5 | BNB | DOWN | 0.71 | open |  |
| 11-05 17:01 | +10 stop | ETH | DOWN | 0.71 | open |  |
| 11-05 17:01 | +20 | ETH | DOWN | 0.71 | open |  |
| 11-05 17:01 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-05 17:01 | +10 | ETH | DOWN | 0.71 | open |  |
| 11-05 17:01 | +5 | ETH | DOWN | 0.71 | open |  |
| 11-05 17:01 | +10 stop | SOL | DOWN | 0.65 | open |  |
| 11-05 17:01 | +20 | SOL | DOWN | 0.65 | open |  |
| 11-05 17:01 | +15 | SOL | DOWN | 0.65 | open |  |
| 11-05 17:01 | +10 | SOL | DOWN | 0.65 | open |  |
| 11-05 17:01 | +5 | SOL | DOWN | 0.65 | 0.72 | 0.39 |
| 11-05 17:01 | +10 stop | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-05 17:01 | +20 | ZEC | DOWN | 0.66 | open |  |
| 11-05 17:01 | +15 | ZEC | DOWN | 0.66 | open |  |
| 11-05 17:01 | +10 | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-05 17:01 | +5 | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-05 17:01 | +10 stop | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-05 17:01 | +20 | DOGE | DOWN | 0.68 | open |  |
| 11-05 17:01 | +15 | DOGE | DOWN | 0.68 | open |  |
| 11-05 17:01 | +10 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-05 17:01 | +5 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-05 16:58 | +10 stop | BNB | UP | 0.66 | 0.79 | 1.02 |
| 11-05 16:56 | +10 stop | BTC | DOWN | 0.58 | 0.76 | 1.49 |
| 11-05 16:55 | +10 stop | BTC | UP | 0.65 | 0.44 | -2.44 |
| 11-05 16:55 | +15 | BTC | UP | 0.65 | no | -6.66 |
| 11-05 16:55 | +10 | BTC | UP | 0.65 | no | -6.66 |
| 11-05 16:55 | +5 | BTC | UP | 0.65 | no | -6.66 |
| 11-05 16:54 | +10 stop | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-05 16:54 | +20 | DOGE | DOWN | 0.55 | 0.81 | 2.31 |
| 11-05 16:54 | +15 | DOGE | DOWN | 0.55 | 0.81 | 2.31 |
| 11-05 16:54 | +10 | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
