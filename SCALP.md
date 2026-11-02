# Range-Scalp Bot

*Updated Mon Nov 02 11:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44781 | 38995 | 5786 (65) | 3 | $-12948.26 | -4.6% |
| **+10¢** | 33424 | 26723 | 6701 (86) | 3 | $-11800.95 | -5.6% |
| **+15¢** | 27964 | 20752 | 7212 (113) | 3 | $-10844.19 | -6.2% |
| **+20¢** | 24847 | 17298 | 7549 (148) | 3 | $-9556.25 | -6.1% |
| **+10¢ (15¢ stop)** | 54650 | 54563 | 87 (51) | 3 | $-20683.28 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 11:30 | +10 stop | ZEC | UP | 0.61 | open |  |
| 11-02 11:30 | +20 | ZEC | UP | 0.61 | open |  |
| 11-02 11:30 | +15 | ZEC | UP | 0.61 | open |  |
| 11-02 11:30 | +10 | ZEC | UP | 0.61 | open |  |
| 11-02 11:30 | +5 | ZEC | UP | 0.61 | open |  |
| 11-02 11:30 | +10 stop | ETH | UP | 0.55 | open |  |
| 11-02 11:30 | +20 | ETH | UP | 0.55 | open |  |
| 11-02 11:30 | +15 | ETH | UP | 0.56 | open |  |
| 11-02 11:30 | +10 | ETH | UP | 0.56 | open |  |
| 11-02 11:30 | +5 | ETH | UP | 0.56 | open |  |
| 11-02 11:30 | +10 stop | XRP | UP | 0.54 | open |  |
| 11-02 11:30 | +20 | XRP | UP | 0.54 | open |  |
| 11-02 11:30 | +15 | XRP | UP | 0.54 | open |  |
| 11-02 11:30 | +10 | XRP | UP | 0.54 | open |  |
| 11-02 11:30 | +5 | XRP | UP | 0.54 | open |  |
| 11-02 11:27 | +10 stop | SOL | UP | 0.53 | 0.28 | -2.83 |
| 11-02 11:26 | +10 stop | SOL | DOWN | 0.36 | 0.54 | 1.45 |
| 11-02 11:25 | +5 | BNB | DOWN | 0.71 | 0.90 | 1.71 |
| 11-02 11:25 | +10 stop | BNB | DOWN | 0.70 | 0.90 | 1.75 |
| 11-02 11:25 | +5 | BNB | UP | 0.46 | 0.56 | 0.64 |
| 11-02 11:24 | +10 stop | BNB | UP | 0.57 | 0.42 | -1.91 |
| 11-02 11:24 | +10 | BNB | UP | 0.57 | no | -5.93 |
| 11-02 11:24 | +5 | BNB | UP | 0.57 | 0.64 | 0.30 |
| 11-02 11:23 | +10 stop | SOL | UP | 0.55 | 0.74 | 1.58 |
| 11-02 11:22 | +5 | XRP | UP | 0.65 | 0.71 | 0.29 |
| 11-02 11:22 | +10 stop | XRP | UP | 0.64 | 0.86 | 1.92 |
| 11-02 11:22 | +10 stop | SOL | DOWN | 0.69 | 0.53 | -1.93 |
| 11-02 11:22 | +20 | SOL | DOWN | 0.69 | 0.97 | 2.58 |
| 11-02 11:22 | +15 | SOL | DOWN | 0.69 | 0.88 | 1.67 |
| 11-02 11:22 | +10 | SOL | DOWN | 0.69 | 0.88 | 1.67 |
| 11-02 11:22 | +5 | SOL | DOWN | 0.69 | 0.88 | 1.67 |
| 11-02 11:21 | +10 stop | NEAR | UP | 0.66 | 0.87 | 1.86 |
| 11-02 11:20 | +10 stop | HYPE | UP | 0.60 | 0.70 | 0.68 |
| 11-02 11:19 | +10 stop | NEAR | DOWN | 0.50 | 0.35 | -1.84 |
| 11-02 11:19 | +10 | NEAR | DOWN | 0.50 | yes | -5.18 |
| 11-02 11:19 | +5 | NEAR | DOWN | 0.49 | yes | -5.08 |
| 11-02 11:19 | +10 stop | XRP | DOWN | 0.66 | 0.48 | -2.09 |
| 11-02 11:18 | +10 stop | HYPE | DOWN | 0.58 | 0.43 | -1.86 |
| 11-02 11:18 | +20 | HYPE | DOWN | 0.58 | yes | -5.98 |
| 11-02 11:18 | +15 | HYPE | DOWN | 0.58 | yes | -5.98 |
