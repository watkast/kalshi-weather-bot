# Range-Scalp Bot

*Updated Tue Nov 03 05:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45603 | 39704 | 5899 (69) | 1 | $-13183.66 | -4.6% |
| **+10¢** | 34037 | 27201 | 6836 (91) | 4 | $-12085.85 | -5.6% |
| **+15¢** | 28482 | 21128 | 7354 (119) | 5 | $-11084.90 | -6.2% |
| **+20¢** | 25297 | 17592 | 7705 (154) | 7 | $-9865.00 | -6.2% |
| **+10¢ (15¢ stop)** | 55643 | 55554 | 89 (53) | 5 | $-20975.19 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 05:02 | +5 | BNB | DOWN | 0.70 | 0.77 | 0.42 |
| 11-03 05:02 | +10 stop | DOGE | DOWN | 0.49 | 0.59 | 0.65 |
| 11-03 05:02 | +20 | DOGE | DOWN | 0.47 | 0.69 | 1.87 |
| 11-03 05:02 | +15 | DOGE | DOWN | 0.47 | 0.69 | 1.87 |
| 11-03 05:02 | +10 | DOGE | DOWN | 0.47 | 0.59 | 0.85 |
| 11-03 05:02 | +5 | DOGE | DOWN | 0.47 | 0.56 | 0.54 |
| 11-03 05:01 | +10 stop | BNB | DOWN | 0.68 | open |  |
| 11-03 05:01 | +20 | BNB | DOWN | 0.66 | open |  |
| 11-03 05:01 | +15 | BNB | DOWN | 0.66 | open |  |
| 11-03 05:01 | +10 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 11-03 05:01 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.19 |
| 11-03 05:01 | +10 stop | XRP | DOWN | 0.66 | open |  |
| 11-03 05:01 | +20 | XRP | DOWN | 0.66 | open |  |
| 11-03 05:01 | +15 | XRP | DOWN | 0.66 | open |  |
| 11-03 05:01 | +10 | XRP | DOWN | 0.66 | open |  |
| 11-03 05:01 | +5 | XRP | DOWN | 0.66 | 0.71 | 0.19 |
| 11-03 05:01 | +10 stop | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 11-03 05:01 | +20 | NEAR | DOWN | 0.60 | open |  |
| 11-03 05:01 | +15 | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 11-03 05:01 | +10 | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 11-03 05:01 | +5 | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 11-03 05:01 | +10 stop | SOL | DOWN | 0.65 | open |  |
| 11-03 05:01 | +20 | SOL | DOWN | 0.65 | open |  |
| 11-03 05:01 | +15 | SOL | DOWN | 0.65 | open |  |
| 11-03 05:01 | +10 | SOL | DOWN | 0.65 | open |  |
| 11-03 05:01 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 11-03 05:01 | +10 stop | ETH | DOWN | 0.66 | open |  |
| 11-03 05:01 | +20 | ETH | DOWN | 0.66 | open |  |
| 11-03 05:01 | +15 | ETH | DOWN | 0.66 | open |  |
| 11-03 05:01 | +10 | ETH | DOWN | 0.66 | open |  |
| 11-03 05:01 | +5 | ETH | DOWN | 0.66 | open |  |
| 11-03 05:01 | +10 stop | ZEC | DOWN | 0.64 | 0.82 | 1.52 |
| 11-03 05:01 | +20 | ZEC | DOWN | 0.65 | open |  |
| 11-03 05:01 | +15 | ZEC | DOWN | 0.65 | 0.82 | 1.43 |
| 11-03 05:01 | +10 | ZEC | DOWN | 0.65 | 0.82 | 1.43 |
| 11-03 05:01 | +5 | ZEC | DOWN | 0.65 | 0.71 | 0.29 |
| 11-03 05:01 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 11-03 05:01 | +20 | BTC | DOWN | 0.64 | open |  |
| 11-03 05:01 | +15 | BTC | DOWN | 0.64 | open |  |
| 11-03 05:01 | +10 | BTC | DOWN | 0.64 | open |  |
