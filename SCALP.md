# Range-Scalp Bot

*Updated Sun Oct 25 04:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32546 | 28379 | 4167 (42) | 5 | $-9268.85 | -4.5% |
| **+10¢** | 24361 | 19535 | 4826 (60) | 5 | $-8308.15 | -5.4% |
| **+15¢** | 20393 | 15201 | 5192 (83) | 5 | $-7462.32 | -5.8% |
| **+20¢** | 18064 | 12631 | 5433 (105) | 7 | $-6603.93 | -5.8% |
| **+10¢ (15¢ stop)** | 39983 | 39923 | 60 (32) | 3 | $-15277.21 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 04:04 | +10 stop | NEAR | UP | 0.64 | open |  |
| 10-25 04:04 | +10 | NEAR | UP | 0.64 | open |  |
| 10-25 04:04 | +5 | NEAR | UP | 0.64 | open |  |
| 10-25 04:03 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 10-25 04:03 | +15 | XRP | DOWN | 0.68 | open |  |
| 10-25 04:03 | +10 | XRP | DOWN | 0.68 | open |  |
| 10-25 04:03 | +10 stop | SOL | DOWN | 0.66 | open |  |
| 10-25 04:03 | +10 | SOL | DOWN | 0.66 | open |  |
| 10-25 04:03 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-25 04:03 | +5 | NEAR | UP | 0.56 | 0.76 | 1.69 |
| 10-25 04:03 | +5 | XRP | DOWN | 0.68 | open |  |
| 10-25 04:02 | +10 stop | ETH | DOWN | 0.63 | 0.43 | -2.35 |
| 10-25 04:02 | +20 | ETH | DOWN | 0.63 | open |  |
| 10-25 04:02 | +15 | ETH | DOWN | 0.63 | open |  |
| 10-25 04:02 | +10 | ETH | DOWN | 0.64 | open |  |
| 10-25 04:02 | +5 | ETH | DOWN | 0.64 | open |  |
| 10-25 04:02 | +5 | BNB | UP | 0.60 | 0.66 | 0.27 |
| 10-25 04:02 | +10 stop | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 10-25 04:02 | +20 | BTC | DOWN | 0.56 | open |  |
| 10-25 04:02 | +15 | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 10-25 04:02 | +10 | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 10-25 04:02 | +5 | BTC | DOWN | 0.56 | 0.63 | 0.35 |
| 10-25 04:01 | +10 stop | SOL | DOWN | 0.59 | 0.69 | 0.68 |
| 10-25 04:01 | +20 | SOL | DOWN | 0.59 | open |  |
| 10-25 04:01 | +15 | SOL | DOWN | 0.59 | open |  |
| 10-25 04:01 | +10 | SOL | DOWN | 0.59 | 0.69 | 0.68 |
| 10-25 04:01 | +5 | SOL | DOWN | 0.59 | 0.69 | 0.68 |
| 10-25 04:01 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-25 04:01 | +20 | XRP | DOWN | 0.57 | open |  |
| 10-25 04:01 | +15 | XRP | DOWN | 0.52 | 0.67 | 1.16 |
| 10-25 04:01 | +10 | XRP | DOWN | 0.52 | 0.67 | 1.16 |
| 10-25 04:01 | +5 | XRP | DOWN | 0.52 | 0.59 | 0.35 |
| 10-25 04:01 | +10 stop | BNB | UP | 0.55 | 0.66 | 0.76 |
| 10-25 04:01 | +20 | BNB | UP | 0.55 | 0.75 | 1.68 |
| 10-25 04:01 | +15 | BNB | UP | 0.55 | 0.75 | 1.68 |
| 10-25 04:01 | +10 | BNB | UP | 0.55 | 0.66 | 0.76 |
| 10-25 04:01 | +5 | BNB | UP | 0.55 | 0.61 | 0.25 |
| 10-25 04:01 | +10 stop | ZEC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-25 04:01 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-25 04:01 | +15 | ZEC | DOWN | 0.60 | 0.77 | 1.40 |
