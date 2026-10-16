# Range-Scalp Bot

*Updated Fri Oct 16 11:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19119 | 16616 | 2503 (28) | 3 | $-5748.37 | -4.8% |
| **+10¢** | 14407 | 11513 | 2894 (40) | 6 | $-5188.32 | -5.7% |
| **+15¢** | 12063 | 8952 | 3111 (59) | 6 | $-4662.33 | -6.2% |
| **+20¢** | 10703 | 7443 | 3260 (78) | 6 | $-4131.86 | -6.1% |
| **+10¢ (15¢ stop)** | 23508 | 23458 | 50 (29) | 6 | $-9062.91 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 11:01 | +5 | XRP | DOWN | 0.54 | 0.62 | 0.45 |
| 10-16 11:01 | +10 stop | DOGE | DOWN | 0.56 | open |  |
| 10-16 11:01 | +20 | DOGE | DOWN | 0.56 | open |  |
| 10-16 11:01 | +15 | DOGE | DOWN | 0.56 | open |  |
| 10-16 11:01 | +10 | DOGE | DOWN | 0.56 | open |  |
| 10-16 11:01 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.25 |
| 10-16 11:01 | +10 stop | SOL | DOWN | 0.58 | open |  |
| 10-16 11:01 | +20 | SOL | DOWN | 0.58 | open |  |
| 10-16 11:01 | +15 | SOL | DOWN | 0.58 | open |  |
| 10-16 11:01 | +10 | SOL | DOWN | 0.58 | open |  |
| 10-16 11:01 | +5 | SOL | DOWN | 0.58 | open |  |
| 10-16 11:01 | +10 stop | HYPE | DOWN | 0.62 | open |  |
| 10-16 11:01 | +20 | HYPE | DOWN | 0.62 | open |  |
| 10-16 11:01 | +15 | HYPE | DOWN | 0.62 | open |  |
| 10-16 11:01 | +10 | HYPE | DOWN | 0.62 | open |  |
| 10-16 11:01 | +5 | HYPE | DOWN | 0.62 | open |  |
| 10-16 11:01 | +5 | ETH | DOWN | 0.60 | open |  |
| 10-16 11:00 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 10-16 11:00 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-16 11:00 | +15 | XRP | DOWN | 0.64 | open |  |
| 10-16 11:00 | +10 | XRP | DOWN | 0.64 | open |  |
| 10-16 11:00 | +5 | XRP | DOWN | 0.64 | 0.71 | 0.38 |
| 10-16 11:00 | +10 stop | ETH | DOWN | 0.60 | open |  |
| 10-16 11:00 | +20 | ETH | DOWN | 0.60 | open |  |
| 10-16 11:00 | +15 | ETH | DOWN | 0.60 | open |  |
| 10-16 11:00 | +10 | ETH | DOWN | 0.60 | open |  |
| 10-16 11:00 | +5 | ETH | DOWN | 0.60 | 0.69 | 0.58 |
| 10-16 11:00 | +10 stop | NEAR | DOWN | 0.66 | open |  |
| 10-16 11:00 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-16 11:00 | +15 | NEAR | DOWN | 0.66 | open |  |
| 10-16 11:00 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-16 11:00 | +5 | NEAR | DOWN | 0.66 | 0.72 | 0.29 |
| 10-16 10:58 | +10 stop | NEAR | DOWN | 0.32 | 0.60 | 2.47 |
| 10-16 10:58 | +20 | NEAR | DOWN | 0.33 | 0.60 | 2.37 |
| 10-16 10:58 | +15 | NEAR | DOWN | 0.33 | 0.60 | 2.37 |
| 10-16 10:58 | +10 | NEAR | DOWN | 0.34 | 0.60 | 2.31 |
| 10-16 10:58 | +5 | NEAR | DOWN | 0.32 | 0.60 | 2.47 |
| 10-16 10:57 | +10 stop | XRP | UP | 0.65 | 0.48 | -2.04 |
| 10-16 10:56 | +10 stop | XRP | DOWN | 0.54 | 0.37 | -2.05 |
| 10-16 10:55 | +10 stop | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
