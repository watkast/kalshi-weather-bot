# Range-Scalp Bot

*Updated Wed Nov 04 00:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46544 | 40531 | 6013 (72) | 5 | $-13366.99 | -4.6% |
| **+10¢** | 34759 | 27788 | 6971 (96) | 5 | $-12212.31 | -5.6% |
| **+15¢** | 29103 | 21605 | 7498 (124) | 5 | $-11155.81 | -6.1% |
| **+20¢** | 25855 | 17999 | 7856 (164) | 6 | $-9842.71 | -6.1% |
| **+10¢ (15¢ stop)** | 56761 | 56668 | 93 (56) | 3 | $-21250.09 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 00:33 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 11-04 00:33 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 11-04 00:33 | +10 stop | BNB | DOWN | 0.67 | open |  |
| 11-04 00:32 | +5 | DOGE | DOWN | 0.67 | 0.73 | 0.30 |
| 11-04 00:32 | +10 stop | NEAR | DOWN | 0.56 | 0.70 | 1.07 |
| 11-04 00:32 | +10 stop | SOL | DOWN | 0.63 | 0.76 | 1.00 |
| 11-04 00:32 | +20 | SOL | DOWN | 0.63 | open |  |
| 11-04 00:32 | +15 | SOL | DOWN | 0.63 | 0.81 | 1.52 |
| 11-04 00:32 | +10 | SOL | DOWN | 0.63 | 0.76 | 1.00 |
| 11-04 00:32 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.28 |
| 11-04 00:32 | +10 stop | BTC | DOWN | 0.58 | 0.70 | 0.87 |
| 11-04 00:32 | +10 stop | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 11-04 00:32 | +20 | DOGE | DOWN | 0.59 | 0.79 | 1.71 |
| 11-04 00:32 | +15 | DOGE | DOWN | 0.60 | 0.79 | 1.61 |
| 11-04 00:32 | +10 | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-04 00:32 | +5 | DOGE | DOWN | 0.60 | 0.66 | 0.27 |
| 11-04 00:31 | +10 stop | HYPE | UP | 0.40 | 0.67 | 2.33 |
| 11-04 00:31 | +20 | HYPE | UP | 0.40 | 0.67 | 2.33 |
| 11-04 00:31 | +15 | HYPE | UP | 0.40 | 0.67 | 2.33 |
| 11-04 00:31 | +10 | HYPE | UP | 0.40 | 0.67 | 2.37 |
| 11-04 00:31 | +5 | HYPE | UP | 0.40 | 0.67 | 2.37 |
| 11-04 00:31 | +10 stop | NEAR | UP | 0.69 | 0.37 | -3.52 |
| 11-04 00:31 | +20 | NEAR | UP | 0.69 | open |  |
| 11-04 00:31 | +15 | NEAR | UP | 0.69 | open |  |
| 11-04 00:31 | +10 | NEAR | UP | 0.70 | open |  |
| 11-04 00:31 | +5 | NEAR | UP | 0.70 | open |  |
| 11-04 00:31 | +10 stop | BNB | UP | 0.69 | 0.45 | -2.73 |
| 11-04 00:31 | +20 | BNB | UP | 0.69 | open |  |
| 11-04 00:31 | +15 | BNB | UP | 0.69 | open |  |
| 11-04 00:31 | +10 | BNB | UP | 0.69 | open |  |
| 11-04 00:31 | +5 | BNB | UP | 0.69 | open |  |
| 11-04 00:31 | +10 stop | ZEC | UP | 0.66 | 0.51 | -1.84 |
| 11-04 00:31 | +20 | ZEC | UP | 0.67 | open |  |
| 11-04 00:31 | +15 | ZEC | UP | 0.67 | open |  |
| 11-04 00:31 | +10 | ZEC | UP | 0.67 | open |  |
| 11-04 00:31 | +5 | ZEC | UP | 0.67 | open |  |
| 11-04 00:31 | +10 stop | ETH | UP | 0.71 | 0.54 | -2.03 |
| 11-04 00:31 | +20 | ETH | UP | 0.71 | open |  |
| 11-04 00:31 | +15 | ETH | UP | 0.71 | open |  |
| 11-04 00:31 | +10 | ETH | UP | 0.71 | open |  |
