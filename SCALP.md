# Range-Scalp Bot

*Updated Tue Nov 17 05:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62611 | 54618 | 7993 (117) | 7 | $-17002.60 | -4.3% |
| **+10¢** | 46758 | 37406 | 9352 (159) | 7 | $-15877.41 | -5.4% |
| **+15¢** | 39191 | 29105 | 10086 (201) | 7 | $-14421.71 | -5.9% |
| **+20¢** | 34934 | 24358 | 10576 (256) | 7 | $-12584.62 | -5.7% |
| **+10¢ (15¢ stop)** | 76207 | 76051 | 156 (92) | 0 | $-28099.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 05:18 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 11-17 05:18 | +10 stop | XRP | UP | 0.52 | 0.37 | -1.85 |
| 11-17 05:17 | +5 | ETH | UP | 0.59 | 0.65 | 0.27 |
| 11-17 05:17 | +10 stop | NEAR | UP | 0.66 | 0.80 | 1.13 |
| 11-17 05:17 | +10 stop | HYPE | UP | 0.63 | 0.76 | 1.00 |
| 11-17 05:17 | +20 | HYPE | UP | 0.63 | 0.84 | 1.83 |
| 11-17 05:17 | +15 | HYPE | UP | 0.63 | 0.81 | 1.52 |
| 11-17 05:17 | +10 | HYPE | UP | 0.63 | 0.76 | 1.00 |
| 11-17 05:17 | +5 | HYPE | UP | 0.63 | 0.76 | 1.00 |
| 11-17 05:17 | +10 stop | ETH | UP | 0.55 | 0.65 | 0.66 |
| 11-17 05:17 | +20 | ETH | UP | 0.55 | 0.77 | 1.89 |
| 11-17 05:17 | +15 | ETH | UP | 0.55 | 0.72 | 1.37 |
| 11-17 05:17 | +10 | ETH | UP | 0.55 | 0.65 | 0.66 |
| 11-17 05:17 | +5 | ETH | UP | 0.55 | 0.60 | 0.15 |
| 11-17 05:17 | +10 stop | ZEC | DOWN | 0.54 | 0.39 | -1.85 |
| 11-17 05:16 | +10 stop | ZEC | DOWN | 0.59 | 0.43 | -1.95 |
| 11-17 05:16 | +20 | ZEC | DOWN | 0.59 | open |  |
| 11-17 05:16 | +15 | ZEC | DOWN | 0.59 | open |  |
| 11-17 05:16 | +10 | ZEC | DOWN | 0.59 | open |  |
| 11-17 05:16 | +5 | ZEC | DOWN | 0.59 | open |  |
| 11-17 05:16 | +10 stop | NEAR | DOWN | 0.51 | 0.35 | -1.94 |
| 11-17 05:16 | +20 | NEAR | DOWN | 0.51 | open |  |
| 11-17 05:16 | +15 | NEAR | DOWN | 0.51 | open |  |
| 11-17 05:16 | +10 | NEAR | DOWN | 0.51 | open |  |
| 11-17 05:16 | +5 | NEAR | DOWN | 0.51 | open |  |
| 11-17 05:16 | +10 stop | BTC | DOWN | 0.57 | 0.41 | -1.95 |
| 11-17 05:16 | +20 | BTC | DOWN | 0.57 | open |  |
| 11-17 05:16 | +15 | BTC | DOWN | 0.57 | open |  |
| 11-17 05:16 | +10 | BTC | DOWN | 0.57 | open |  |
| 11-17 05:16 | +5 | BTC | DOWN | 0.57 | open |  |
| 11-17 05:16 | +10 stop | BNB | DOWN | 0.58 | 0.41 | -2.05 |
| 11-17 05:16 | +20 | BNB | DOWN | 0.58 | open |  |
| 11-17 05:16 | +15 | BNB | DOWN | 0.58 | open |  |
| 11-17 05:16 | +10 | BNB | DOWN | 0.58 | open |  |
| 11-17 05:16 | +5 | BNB | DOWN | 0.58 | open |  |
| 11-17 05:16 | +10 stop | SOL | DOWN | 0.66 | 0.48 | -2.14 |
| 11-17 05:16 | +20 | SOL | DOWN | 0.66 | open |  |
| 11-17 05:16 | +15 | SOL | DOWN | 0.66 | open |  |
| 11-17 05:16 | +10 | SOL | DOWN | 0.66 | open |  |
| 11-17 05:16 | +5 | SOL | DOWN | 0.66 | open |  |
