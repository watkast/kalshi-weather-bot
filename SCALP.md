# Range-Scalp Bot

*Updated Fri Oct 30 04:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40173 | 35093 | 5080 (51) | 1 | $-11008.35 | -4.4% |
| **+10¢** | 29935 | 24056 | 5879 (74) | 2 | $-9755.99 | -5.2% |
| **+15¢** | 25039 | 18712 | 6327 (101) | 3 | $-8742.19 | -5.6% |
| **+20¢** | 22219 | 15586 | 6633 (130) | 3 | $-7652.80 | -5.5% |
| **+10¢ (15¢ stop)** | 48993 | 48923 | 70 (37) | 1 | $-18483.14 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 04:17 | +10 stop | XRP | UP | 0.62 | 0.77 | 1.20 |
| 10-30 04:17 | +10 stop | BNB | UP | 0.68 | open |  |
| 10-30 04:17 | +20 | BNB | UP | 0.69 | open |  |
| 10-30 04:17 | +15 | BNB | UP | 0.70 | open |  |
| 10-30 04:17 | +10 | BNB | UP | 0.69 | open |  |
| 10-30 04:17 | +5 | BNB | UP | 0.64 | open |  |
| 10-30 04:17 | +20 | XRP | UP | 0.71 | open |  |
| 10-30 04:17 | +15 | XRP | UP | 0.71 | open |  |
| 10-30 04:17 | +10 | XRP | UP | 0.71 | open |  |
| 10-30 04:17 | +5 | XRP | UP | 0.71 | 0.77 | 0.32 |
| 10-30 04:16 | +10 stop | ETH | DOWN | 0.38 | 0.56 | 1.45 |
| 10-30 04:16 | +10 | ETH | DOWN | 0.38 | 0.56 | 1.45 |
| 10-30 04:16 | +5 | ETH | DOWN | 0.38 | 0.56 | 1.45 |
| 10-30 04:16 | +10 stop | SOL | DOWN | 0.43 | 0.53 | 0.64 |
| 10-30 04:16 | +20 | SOL | DOWN | 0.43 | open |  |
| 10-30 04:16 | +15 | SOL | DOWN | 0.43 | open |  |
| 10-30 04:16 | +10 | SOL | DOWN | 0.43 | 0.53 | 0.64 |
| 10-30 04:16 | +5 | SOL | DOWN | 0.43 | 0.53 | 0.64 |
| 10-30 04:16 | +10 stop | HYPE | UP | 0.55 | 0.67 | 0.86 |
| 10-30 04:16 | +20 | HYPE | UP | 0.55 | 0.80 | 2.20 |
| 10-30 04:16 | +15 | HYPE | UP | 0.55 | 0.74 | 1.58 |
| 10-30 04:16 | +10 | HYPE | UP | 0.55 | 0.67 | 0.86 |
| 10-30 04:16 | +5 | HYPE | UP | 0.55 | 0.67 | 0.86 |
| 10-30 04:15 | +10 stop | NEAR | UP | 0.55 | 0.66 | 0.77 |
| 10-30 04:15 | +20 | NEAR | UP | 0.55 | 0.85 | 2.74 |
| 10-30 04:15 | +15 | NEAR | UP | 0.55 | 0.85 | 2.73 |
| 10-30 04:15 | +10 | NEAR | UP | 0.55 | 0.66 | 0.76 |
| 10-30 04:15 | +5 | NEAR | UP | 0.55 | 0.66 | 0.76 |
| 10-30 04:15 | +10 stop | ETH | UP | 0.51 | 0.65 | 1.06 |
| 10-30 04:15 | +20 | ETH | UP | 0.51 | 0.76 | 2.19 |
| 10-30 04:15 | +15 | ETH | UP | 0.52 | 0.76 | 2.09 |
| 10-30 04:15 | +10 | ETH | UP | 0.52 | 0.65 | 0.96 |
| 10-30 04:15 | +5 | ETH | UP | 0.52 | 0.65 | 0.96 |
| 10-30 04:01 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 04:01 | +20 | BNB | DOWN | 0.65 | 0.87 | 1.96 |
| 10-30 04:01 | +15 | BNB | DOWN | 0.65 | 0.87 | 1.96 |
| 10-30 04:01 | +10 | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 04:01 | +5 | BNB | DOWN | 0.65 | 0.74 | 0.60 |
| 10-30 04:01 | +10 stop | NEAR | DOWN | 0.64 | 0.76 | 0.93 |
| 10-30 04:01 | +20 | NEAR | DOWN | 0.64 | 0.87 | 2.08 |
