# Range-Scalp Bot

*Updated Wed Nov 04 01:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46568 | 40550 | 6018 (72) | 0 | $-13388.83 | -4.6% |
| **+10¢** | 34781 | 27805 | 6976 (96) | 1 | $-12225.79 | -5.6% |
| **+15¢** | 29125 | 21622 | 7503 (124) | 1 | $-11164.53 | -6.1% |
| **+20¢** | 25876 | 18015 | 7861 (164) | 2 | $-9846.48 | -6.1% |
| **+10¢ (15¢ stop)** | 56785 | 56692 | 93 (56) | 0 | $-21232.78 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 01:02 | +10 stop | ZEC | UP | 0.30 | 0.53 | 1.97 |
| 11-04 01:02 | +10 stop | SOL | UP | 0.38 | 0.55 | 1.35 |
| 11-04 01:02 | +20 | SOL | UP | 0.39 | open |  |
| 11-04 01:02 | +15 | SOL | UP | 0.39 | 0.55 | 1.25 |
| 11-04 01:02 | +10 | SOL | UP | 0.39 | 0.55 | 1.25 |
| 11-04 01:02 | +5 | SOL | UP | 0.39 | 0.55 | 1.25 |
| 11-04 01:01 | +10 stop | BNB | UP | 0.56 | 0.21 | -3.79 |
| 11-04 01:01 | +20 | BNB | UP | 0.56 | open |  |
| 11-04 01:01 | +15 | BNB | UP | 0.56 | open |  |
| 11-04 01:01 | +10 | BNB | UP | 0.56 | open |  |
| 11-04 01:01 | +5 | BNB | UP | 0.56 | 0.62 | 0.26 |
| 11-04 01:01 | +10 stop | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 11-04 01:01 | +20 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 11-04 01:01 | +15 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 11-04 01:01 | +10 | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 11-04 01:01 | +5 | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 11-04 01:01 | +10 stop | ZEC | DOWN | 0.63 | 0.40 | -2.64 |
| 11-04 01:01 | +20 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-04 01:01 | +15 | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-04 01:01 | +10 | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-04 01:01 | +5 | ZEC | DOWN | 0.62 | 0.71 | 0.58 |
| 11-04 01:01 | +10 stop | NEAR | DOWN | 0.63 | 0.82 | 1.62 |
| 11-04 01:01 | +20 | NEAR | DOWN | 0.61 | 0.82 | 1.82 |
| 11-04 01:01 | +15 | NEAR | DOWN | 0.61 | 0.82 | 1.82 |
| 11-04 01:01 | +10 | NEAR | DOWN | 0.61 | 0.82 | 1.82 |
| 11-04 01:01 | +5 | NEAR | DOWN | 0.61 | 0.82 | 1.82 |
| 11-04 01:01 | +10 stop | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 01:01 | +20 | HYPE | DOWN | 0.63 | 0.88 | 2.25 |
| 11-04 01:01 | +15 | HYPE | DOWN | 0.63 | 0.81 | 1.52 |
| 11-04 01:01 | +10 | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 01:01 | +5 | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 01:01 | +10 stop | ETH | DOWN | 0.64 | 0.86 | 1.94 |
| 11-04 01:01 | +20 | ETH | DOWN | 0.64 | 0.86 | 1.94 |
| 11-04 01:01 | +15 | ETH | DOWN | 0.64 | 0.86 | 1.94 |
| 11-04 01:01 | +10 | ETH | DOWN | 0.64 | 0.86 | 1.94 |
| 11-04 01:01 | +5 | ETH | DOWN | 0.64 | 0.72 | 0.48 |
| 11-04 01:01 | +10 stop | DOGE | DOWN | 0.66 | 0.80 | 1.12 |
| 11-04 01:01 | +20 | DOGE | DOWN | 0.66 | 0.86 | 1.75 |
| 11-04 01:01 | +15 | DOGE | DOWN | 0.66 | 0.86 | 1.75 |
| 11-04 01:01 | +10 | DOGE | DOWN | 0.66 | 0.80 | 1.12 |
