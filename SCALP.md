# Range-Scalp Bot

*Updated Thu Oct 29 18:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39605 | 34579 | 5026 (50) | 0 | $-10980.44 | -4.4% |
| **+10¢** | 29520 | 23707 | 5813 (73) | 1 | $-9747.17 | -5.2% |
| **+15¢** | 24681 | 18430 | 6251 (100) | 1 | $-8738.48 | -5.6% |
| **+20¢** | 21901 | 15353 | 6548 (129) | 2 | $-7618.80 | -5.5% |
| **+10¢ (15¢ stop)** | 48364 | 48294 | 70 (37) | 1 | $-18345.95 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 18:39 | +5 | HYPE | UP | 0.57 | 0.62 | 0.15 |
| 10-29 18:39 | +10 stop | HYPE | UP | 0.61 | open |  |
| 10-29 18:39 | +5 | HYPE | UP | 0.61 | 0.68 | 0.37 |
| 10-29 18:38 | +10 stop | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 10-29 18:38 | +20 | BNB | DOWN | 0.59 | 0.82 | 2.02 |
| 10-29 18:38 | +15 | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 10-29 18:38 | +10 | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 10-29 18:38 | +5 | BNB | DOWN | 0.59 | 0.69 | 0.63 |
| 10-29 18:37 | +5 | ZEC | DOWN | 0.71 | 0.78 | 0.42 |
| 10-29 18:35 | +10 stop | HYPE | DOWN | 0.66 | 0.38 | -3.13 |
| 10-29 18:35 | +10 | HYPE | DOWN | 0.66 | open |  |
| 10-29 18:35 | +5 | HYPE | DOWN | 0.67 | 0.74 | 0.40 |
| 10-29 18:33 | +10 stop | HYPE | DOWN | 0.56 | 0.67 | 0.73 |
| 10-29 18:33 | +10 | HYPE | DOWN | 0.57 | 0.67 | 0.67 |
| 10-29 18:33 | +5 | HYPE | DOWN | 0.57 | 0.67 | 0.67 |
| 10-29 18:31 | +10 stop | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 10-29 18:31 | +20 | ZEC | DOWN | 0.70 | open |  |
| 10-29 18:31 | +15 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 10-29 18:31 | +10 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 10-29 18:31 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-29 18:31 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-29 18:31 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.87 |
| 10-29 18:31 | +15 | XRP | DOWN | 0.70 | 0.91 | 1.87 |
| 10-29 18:31 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-29 18:31 | +5 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-29 18:31 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.83 |
| 10-29 18:31 | +15 | SOL | DOWN | 0.70 | 0.91 | 1.83 |
| 10-29 18:31 | +10 | SOL | DOWN | 0.70 | 0.84 | 1.15 |
| 10-29 18:31 | +5 | SOL | DOWN | 0.70 | 0.84 | 1.15 |
| 10-29 18:31 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-29 18:31 | +20 | HYPE | DOWN | 0.67 | open |  |
| 10-29 18:31 | +15 | HYPE | DOWN | 0.67 | open |  |
| 10-29 18:31 | +10 | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-29 18:31 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.30 |
| 10-29 18:31 | +10 stop | BNB | DOWN | 0.62 | 0.85 | 2.04 |
| 10-29 18:31 | +20 | BNB | DOWN | 0.62 | 0.85 | 2.04 |
| 10-29 18:31 | +15 | BNB | DOWN | 0.62 | 0.85 | 2.04 |
| 10-29 18:31 | +10 | BNB | DOWN | 0.62 | 0.85 | 2.04 |
| 10-29 18:31 | +5 | BNB | DOWN | 0.62 | 0.69 | 0.38 |
| 10-29 18:26 | +5 | BTC | UP | 0.33 | 0.56 | 1.96 |
