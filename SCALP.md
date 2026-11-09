# Range-Scalp Bot

*Updated Mon Nov 09 01:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53119 | 46326 | 6793 (85) | 5 | $-14608.62 | -4.4% |
| **+10¢** | 39658 | 31734 | 7924 (110) | 6 | $-13605.48 | -5.5% |
| **+15¢** | 33231 | 24695 | 8536 (141) | 6 | $-12394.71 | -5.9% |
| **+20¢** | 29557 | 20606 | 8951 (186) | 6 | $-10913.47 | -5.9% |
| **+10¢ (15¢ stop)** | 64691 | 64585 | 106 (63) | 0 | $-23953.57 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 01:37 | +10 stop | XRP | UP | 0.65 | 0.75 | 0.70 |
| 11-09 01:37 | +10 stop | HYPE | DOWN | 0.57 | 0.32 | -2.87 |
| 11-09 01:37 | +10 stop | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 11-09 01:37 | +20 | ZEC | UP | 0.71 | 0.96 | 2.32 |
| 11-09 01:37 | +15 | ZEC | UP | 0.71 | 0.89 | 1.58 |
| 11-09 01:37 | +10 | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 11-09 01:37 | +5 | ZEC | UP | 0.71 | 0.80 | 0.63 |
| 11-09 01:37 | +10 stop | BTC | UP | 0.68 | 0.78 | 0.71 |
| 11-09 01:34 | +10 stop | BNB | UP | 0.70 | 0.81 | 0.82 |
| 11-09 01:33 | +10 stop | BTC | UP | 0.66 | 0.78 | 0.91 |
| 11-09 01:33 | +10 stop | DOGE | UP | 0.70 | 0.83 | 1.05 |
| 11-09 01:33 | +10 stop | XRP | UP | 0.65 | 0.77 | 0.91 |
| 11-09 01:33 | +10 stop | HYPE | UP | 0.57 | 0.70 | 0.97 |
| 11-09 01:33 | +20 | NEAR | UP | 0.70 | 0.94 | 2.17 |
| 11-09 01:33 | +15 | NEAR | UP | 0.66 | 0.83 | 1.44 |
| 11-09 01:32 | +10 stop | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 11-09 01:32 | +10 | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 11-09 01:32 | +5 | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 11-09 01:32 | +10 stop | BNB | DOWN | 0.63 | 0.46 | -2.05 |
| 11-09 01:32 | +10 | BNB | DOWN | 0.62 | open |  |
| 11-09 01:32 | +5 | BNB | DOWN | 0.62 | open |  |
| 11-09 01:31 | +10 stop | XRP | DOWN | 0.60 | 0.33 | -3.03 |
| 11-09 01:31 | +20 | XRP | DOWN | 0.58 | open |  |
| 11-09 01:31 | +15 | XRP | DOWN | 0.58 | open |  |
| 11-09 01:31 | +10 | XRP | DOWN | 0.57 | open |  |
| 11-09 01:31 | +5 | XRP | DOWN | 0.57 | open |  |
| 11-09 01:31 | +10 stop | SOL | DOWN | 0.50 | 0.28 | -2.53 |
| 11-09 01:31 | +20 | SOL | DOWN | 0.50 | open |  |
| 11-09 01:31 | +15 | SOL | DOWN | 0.50 | open |  |
| 11-09 01:31 | +10 | SOL | DOWN | 0.50 | open |  |
| 11-09 01:31 | +5 | SOL | DOWN | 0.50 | 0.58 | 0.44 |
| 11-09 01:31 | +10 stop | HYPE | DOWN | 0.57 | 0.37 | -2.35 |
| 11-09 01:31 | +20 | HYPE | DOWN | 0.57 | open |  |
| 11-09 01:31 | +15 | HYPE | DOWN | 0.57 | open |  |
| 11-09 01:31 | +10 | HYPE | DOWN | 0.57 | open |  |
| 11-09 01:31 | +5 | HYPE | DOWN | 0.57 | open |  |
| 11-09 01:31 | +10 stop | BTC | DOWN | 0.61 | 0.46 | -1.85 |
| 11-09 01:31 | +20 | BTC | DOWN | 0.61 | open |  |
| 11-09 01:31 | +15 | BTC | DOWN | 0.61 | open |  |
| 11-09 01:31 | +10 | BTC | DOWN | 0.61 | open |  |
