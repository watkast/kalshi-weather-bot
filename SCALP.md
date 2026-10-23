# Range-Scalp Bot

*Updated Fri Oct 23 01:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29569 | 25738 | 3831 (39) | 5 | $-8726.35 | -4.7% |
| **+10¢** | 22172 | 17737 | 4435 (55) | 6 | $-7854.30 | -5.6% |
| **+15¢** | 18563 | 13802 | 4761 (78) | 7 | $-7028.69 | -6.0% |
| **+20¢** | 16427 | 11437 | 4990 (100) | 7 | $-6365.15 | -6.2% |
| **+10¢ (15¢ stop)** | 36321 | 36262 | 59 (32) | 1 | $-13734.13 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 01:23 | +5 | BTC | DOWN | 0.52 | 0.59 | 0.35 |
| 10-23 01:23 | +10 stop | ETH | UP | 0.60 | 0.40 | -2.34 |
| 10-23 01:22 | +10 stop | NEAR | UP | 0.70 | 0.55 | -1.83 |
| 10-23 01:22 | +10 stop | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 10-23 01:22 | +10 | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 10-23 01:22 | +5 | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 10-23 01:21 | +10 stop | BTC | DOWN | 0.55 | open |  |
| 10-23 01:21 | +20 | BTC | DOWN | 0.55 | open |  |
| 10-23 01:21 | +15 | BTC | DOWN | 0.56 | open |  |
| 10-23 01:21 | +10 | BTC | DOWN | 0.56 | open |  |
| 10-23 01:21 | +5 | BTC | DOWN | 0.56 | 0.64 | 0.45 |
| 10-23 01:21 | +10 stop | HYPE | DOWN | 0.41 | 0.55 | 1.05 |
| 10-23 01:21 | +10 | HYPE | DOWN | 0.41 | 0.55 | 1.05 |
| 10-23 01:21 | +5 | HYPE | DOWN | 0.41 | 0.55 | 1.05 |
| 10-23 01:21 | +10 stop | SOL | UP | 0.66 | 0.80 | 1.12 |
| 10-23 01:21 | +10 stop | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-23 01:21 | +20 | HYPE | DOWN | 0.58 | open |  |
| 10-23 01:21 | +15 | HYPE | DOWN | 0.58 | open |  |
| 10-23 01:21 | +10 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-23 01:21 | +5 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-23 01:21 | +10 stop | XRP | DOWN | 0.58 | 0.36 | -2.55 |
| 10-23 01:21 | +20 | XRP | DOWN | 0.59 | open |  |
| 10-23 01:21 | +15 | XRP | DOWN | 0.59 | open |  |
| 10-23 01:21 | +10 | XRP | DOWN | 0.58 | open |  |
| 10-23 01:21 | +5 | XRP | DOWN | 0.58 | open |  |
| 10-23 01:20 | +10 stop | BNB | DOWN | 0.57 | 0.38 | -2.29 |
| 10-23 01:20 | +20 | BNB | DOWN | 0.57 | open |  |
| 10-23 01:20 | +15 | BNB | DOWN | 0.57 | open |  |
| 10-23 01:20 | +10 | BNB | DOWN | 0.57 | open |  |
| 10-23 01:20 | +5 | BNB | DOWN | 0.57 | open |  |
| 10-23 01:20 | +10 stop | ETH | DOWN | 0.66 | 0.45 | -2.44 |
| 10-23 01:20 | +20 | ETH | DOWN | 0.66 | open |  |
| 10-23 01:20 | +15 | ETH | DOWN | 0.66 | open |  |
| 10-23 01:20 | +10 | ETH | DOWN | 0.66 | open |  |
| 10-23 01:20 | +5 | ETH | DOWN | 0.66 | open |  |
| 10-23 01:19 | +10 stop | SOL | DOWN | 0.70 | 0.43 | -3.03 |
| 10-23 01:19 | +20 | SOL | DOWN | 0.70 | open |  |
| 10-23 01:19 | +15 | SOL | DOWN | 0.70 | open |  |
| 10-23 01:19 | +10 | SOL | DOWN | 0.70 | open |  |
| 10-23 01:19 | +5 | SOL | DOWN | 0.70 | open |  |
