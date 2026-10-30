# Range-Scalp Bot

*Updated Fri Oct 30 01:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39994 | 34934 | 5060 (51) | 3 | $-10961.09 | -4.4% |
| **+10¢** | 29806 | 23954 | 5852 (74) | 3 | $-9688.81 | -5.2% |
| **+15¢** | 24924 | 18629 | 6295 (101) | 4 | $-8673.10 | -5.5% |
| **+20¢** | 22116 | 15515 | 6601 (130) | 4 | $-7594.76 | -5.5% |
| **+10¢ (15¢ stop)** | 48806 | 48736 | 70 (37) | 1 | $-18438.35 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 01:08 | +5 | BNB | UP | 0.69 | 0.75 | 0.31 |
| 10-30 01:07 | +10 stop | BNB | UP | 0.61 | 0.75 | 1.09 |
| 10-30 01:07 | +15 | BNB | UP | 0.61 | open |  |
| 10-30 01:07 | +10 | BNB | UP | 0.62 | 0.75 | 0.95 |
| 10-30 01:07 | +5 | BNB | UP | 0.63 | 0.68 | 0.17 |
| 10-30 01:07 | +10 stop | DOGE | DOWN | 0.68 | 0.48 | -2.34 |
| 10-30 01:05 | +10 stop | NEAR | DOWN | 0.52 | open |  |
| 10-30 01:05 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-30 01:05 | +10 stop | ZEC | DOWN | 0.54 | 0.67 | 0.96 |
| 10-30 01:03 | +10 stop | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 10-30 01:03 | +20 | BNB | DOWN | 0.59 | open |  |
| 10-30 01:03 | +15 | BNB | DOWN | 0.60 | 0.78 | 1.51 |
| 10-30 01:03 | +10 | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 10-30 01:03 | +5 | BNB | DOWN | 0.60 | 0.69 | 0.58 |
| 10-30 01:02 | +10 stop | XRP | DOWN | 0.63 | 0.77 | 1.10 |
| 10-30 01:02 | +20 | XRP | DOWN | 0.64 | 0.85 | 1.84 |
| 10-30 01:02 | +15 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-30 01:02 | +10 | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 10-30 01:02 | +5 | XRP | DOWN | 0.64 | 0.70 | 0.28 |
| 10-30 01:02 | +10 stop | SOL | DOWN | 0.61 | 0.73 | 0.89 |
| 10-30 01:02 | +20 | SOL | DOWN | 0.62 | 0.83 | 1.83 |
| 10-30 01:02 | +15 | SOL | DOWN | 0.62 | 0.77 | 1.20 |
| 10-30 01:02 | +10 | SOL | DOWN | 0.62 | 0.73 | 0.79 |
| 10-30 01:02 | +5 | SOL | DOWN | 0.62 | 0.69 | 0.38 |
| 10-30 01:02 | +10 stop | ZEC | UP | 0.69 | 0.49 | -2.33 |
| 10-30 01:02 | +20 | ZEC | UP | 0.68 | open |  |
| 10-30 01:02 | +15 | ZEC | UP | 0.69 | open |  |
| 10-30 01:02 | +10 | ZEC | UP | 0.69 | open |  |
| 10-30 01:02 | +5 | ZEC | UP | 0.69 | open |  |
| 10-30 01:01 | +5 | DOGE | UP | 0.58 | open |  |
| 10-30 01:01 | +10 stop | NEAR | UP | 0.69 | 0.52 | -2.03 |
| 10-30 01:01 | +20 | NEAR | UP | 0.69 | open |  |
| 10-30 01:01 | +15 | NEAR | UP | 0.69 | open |  |
| 10-30 01:01 | +10 | NEAR | UP | 0.69 | open |  |
| 10-30 01:01 | +5 | NEAR | UP | 0.69 | open |  |
| 10-30 01:01 | +10 stop | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 10-30 01:01 | +20 | ETH | DOWN | 0.60 | 0.82 | 1.92 |
| 10-30 01:01 | +15 | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 10-30 01:01 | +10 | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 10-30 01:01 | +5 | ETH | DOWN | 0.60 | 0.68 | 0.47 |
